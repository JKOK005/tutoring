import numpy as np
import os
import pandas as pd
import scipy as sp
from scipy import optimize
from scipy.stats import linregress

def parse_file_to_dataframe(csv_path: str) -> pd.DataFrame:
	"""
	Attempts to read a CSV file from a given path and returns the dataframe from the parsed file

	Parameters:
		file_path (str): Absolute path to file

	Returns: 
		pd.DataFrame - Parsed dataframe 
	"""
	return pd.read_csv(csv_path)

def init_guess(n_params: int) -> [float]:
	"""
	Generates an initial guess of parameters

	Parameters:
		n_params (int): Number of parameters to generate in the array

	Returns:
		[float] - n_params of elements, each of type float
	"""
	return [0.01] * n_params

def linear_gaussian(x, a, b, mu, sig, m, c):
	"""
	Linear gaussian function implementation
	"""
	gaussian 	= a * sp.exp(-(x-mu)**2 / (2 * sig**2))
	linear 		= m * x + c
	return gaussian + linear

def get_optimal_mu(fnct, x_data: np.array, y_data: np.array, init_guess: [float]):
	"""
	Performs curve fitting to obtain the mean of the gaussian function
	"""
	param_opt, param_covar = optimize.curve_fit(fnct, x_data, y_data, init_guess)
	return param_opt[2]

def compute_velocity(lambda_0: float) -> float:
	"""
	TODO: Implement velocity computation
	"""
	pass

def clean_halpha_spectral_data(halpha_df: pd.DataFrame) -> (np.array, pd.DataFrame):
	""" 
	1) Separate the "Wavelength" column from the dataframe
	2) Transpose observation columns to rows
	3) Collapse all observation data into a single numpy array

	Parameters:
		halpha_df (pd.DataFrame): Original Halpha dataframe

	Returns: 
		np.array 	- Numpy array of wavelength values
		pd.DataFrame - Reformatted dataframe
	"""
	wavelength_df 	= halpha_df["# Wavelength (m) "]
	remaining_df 	= halpha_df.drop(["# Wavelength (m) "], axis = 1) 	# Axis 1 = drop by column
	remaining_df 	= remaining_df.T.reset_index()
	
	observation_df  = remaining_df[["index"]].apply(lambda row: row["index"].replace("Observation: ", ""), axis = 1)
	intensity_df 	= remaining_df.drop(["index"], axis = 1).apply(lambda row: row.to_numpy(), axis = 1)

	observation_df 	= pd.DataFrame(observation_df, columns = ["id"])
	intensity_df 	= pd.DataFrame(intensity_df, columns = ["intensities"])

	final_df 		= pd.concat([observation_df, intensity_df], axis = 1)
	return (wavelength_df.to_numpy(), final_df)

if __name__ == "__main__":
	# Declares that we should run this part of the function when invoking python over the script
	distance_df 	= parse_file_to_dataframe(os.path.join(os.getcwd(), "resources", "Distance_Mpc.csv"))
	halpha_df 		= parse_file_to_dataframe(os.path.join(os.getcwd(), "resources", "Halpha_spectral_data.csv"))

	# Parse spectral dataframe to extract constant wavelenght and variable intensities per plot
	(wavelenghts, halpha_parsed_df) = clean_halpha_spectral_data(halpha_df = halpha_df)

	# Predict lambda_0 for each intensity data point
	halpha_parsed_df["lambda_0"] = halpha_parsed_df.apply(
									lambda row: get_optimal_mu(	fnct = linear_gaussian, 
																x_data = wavelenghts, 
																y_data = row["intensities"], 
																init_guess = init_guess(n_params = 6)
															),
									axis = 1
								)
	halpha_parsed_df["id"] 	= halpha_parsed_df["id"].astype(int)

	# Compute the velocity given lambda_0 and lambda_e
	halpha_parsed_df["velocity"] = halpha_parsed_df.apply(lambda row: compute_velocity(lambda_0 = row["lambda_0"]), axis = 1)

	# Prepare distance dataframe 
	distance_df["Observation"] = distance_df["Observation"].astype(int) 		# We want integer for IDs
	distance_df = distance_df[distance_df["Valid Instrument Response"] == 1] 	# we want only valid responses

	# Join with halpha_parsed_df
	merged_df 	= halpha_parsed_df.merge(distance_df, how = "inner", left_on = "id", right_on = "Observation")

	# Perform linear fitting
	distances 	= merged_df["Distance(Mpc)"].to_numpy()
	velocities 	= merged_df["velocity"].to_numpy()
	res 		= linregress(x = distances, y = velocities)
	print(res)
	print("H_alpha is {0}".formatted(res.slope))
