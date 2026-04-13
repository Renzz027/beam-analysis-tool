import matplotlib.pyplot as plt
import time

SS_Beam_Data = list()
Unified_Load_Structure = list()
Load_Data = list()
Distance = list()
Shear = list()
Moment = list()

def simply_supported_input():
	global SS_Beam_Data
	while True:
		try:
			print("\nPART-2: Input of beam parameters")
			print("Enter the following Beam Prameters: ")
			L = float(input("Enter beam length L in meters (m): "))
			if L <= 0:
				print("Beam length should be positive!")
				continue
			DR_1 = float(input("Enter position of R1 from left in meters (m): "))
			DR_2 = float(input("Enter position of R2 from left in meters (m): "))
			if DR_1 < 0 or DR_1 > L:
				print("Position of R1 should located from 0 - L!")
				continue
			elif DR_2 < 0 or DR_2 > L:
				print("Position of R2 should located from 0 - L!")
				continue
			elif DR_1 == DR_2:
				print("Position of R1 and R2 should not be the same!")
				continue
			elif DR_1 > DR_2:
				print("Position of R2 should be grater than R1 (R2 > R1)!")
				continue

			SS_Beam_Data.append(L)
			SS_Beam_Data.append(DR_1)
			SS_Beam_Data.append(DR_2)
			print("--> Beam length and position of reactions was successfully added!")
			break

		except ValueError:
			print("Please enter a numeric value!")

def fixed_support_input():
	global SS_Beam_Data
	while True:
		try:
			print("\nPART-2: Input of beam parameters")
			print("Enter the following Beam Prameters: ")
			L = float(input("Enter beam length L in meters (m): "))
			if L <= 0:
				print("Beam length should be positive!")
				continue
			SS_Beam_Data.append(L)
			print("--> Beam length was successfully added!")
			break

		except ValueError:
			print("Please enter a numeric value!")

def left_fixed_reaction():
	global Unified_Load_Structure, Load_Data, SS_Beam_Data
	print("\nPART-5: Calculation of Reactions")
	print("--> Calculating reactions....")
	time.sleep(2.5)
	Moment_Sum = 0
	Shear_Sum = 0
	for n in Unified_Load_Structure:
		if n[0] == "Moment":
			if n[2] == "CW":
				Moment_Sum += n[1]
			elif n[2] == "CCW":
				Moment_Sum -= n[1]
		else:
			Moment_Sum += n[5] * n[4]
			Shear_Sum += n[5]
	Moment_reaction = Moment_Sum
	Reaction = Shear_Sum

	SS_Beam_Data.append(Reaction)
	SS_Beam_Data.append(0)
	SS_Beam_Data.append(Moment_reaction)

	Load_Data.append("Reaction_1")
	Load_Data.append(Reaction)
	Load_Data.append(0)
	Unified_Load_Structure.append(Load_Data)
	Load_Data = []

	Load_Data.append("Moment_Reaction")
	Load_Data.append(Moment_reaction)
	Load_Data.append(0)
	Load_Data.append("CCW")
	Unified_Load_Structure.append(Load_Data)
	Load_Data = []
	print("--> Reactions was calculated successfully!")

def right_fixed_reaction():
	global Unified_Load_Structure, Load_Data, SS_Beam_Data
	print("\nPART-5: Calculation of Reactions")
	print("--> Calculating reactions....")
	time.sleep(2.5)
	Moment_Sum = 0
	Shear_Sum = 0
	for n in Unified_Load_Structure:
		if n[0] == "Moment":
			if n[2] == "CW":
				Moment_Sum -= n[1]
			elif n[2] == "CCW":
				Moment_Sum += n[1]
		else:
			Moment_Sum += n[5] * (SS_Beam_Data[0] - n[4])
			Shear_Sum += n[5]
	Moment_reaction = Moment_Sum
	Reaction = Shear_Sum

	SS_Beam_Data.append(0)
	SS_Beam_Data.append(Reaction)
	SS_Beam_Data.append(Moment_reaction)

	Load_Data.append("Reaction_2")
	Load_Data.append(Reaction)
	Load_Data.append(SS_Beam_Data[0])
	Unified_Load_Structure.append(Load_Data)
	Load_Data = []

	Load_Data.append("Moment_Reaction")
	Load_Data.append(Moment_reaction)
	Load_Data.append(SS_Beam_Data[0])
	Load_Data.append("CW")
	Unified_Load_Structure.append(Load_Data)
	Load_Data = []
	print("--> Reactions was calculated successfully!")
			
def point_load_input():
	global Unified_Load_Structure, Load_Data, SS_Beam_Data
	while True:
		try:
			print("\n--> Point Load")
			P = float(input("Enter Point Load P (KN): "))
			if P <= 0:
				print("Please enter a positive load value!")
				continue
			DP = float(input("Enter point load distance (m) from the left: "))
			if DP < 0 or DP > SS_Beam_Data[0]:
				print("Please enter load distance between 0 - L!")
				continue

			Load_Data.append("Point Load")
			Load_Data.append(P)
			Load_Data.append(DP)
			Load_Data.append(DP)
			Load_Data.append(DP)
			Load_Data.append(P)
			Unified_Load_Structure.append(Load_Data)
			Load_Data = []
			print("--> Point Load was successfully added to the beam!")
			break

		except ValueError:
			print("Please enter a numeric input!")

def UDL_input():
	global Unified_Load_Structure, Load_Data, SS_Beam_Data
	while True:
		try:
			print("\n--> Uniform Distributed Load")
			W = float(input("Enter Uniformly Distributed Load W (KN/m): "))
			if W <= 0:
				print("Please enter a positive UDL value!")
				continue
			DW_1 = float(input("Enter the start position of UDL (DW_1) from the left (m): "))
			DW_2 = float(input("Enter the end position of UDL (DW_2) from the left (m): "))
			if DW_1 < 0 or DW_2 < 0 or DW_1 > SS_Beam_Data[0] or DW_2 > SS_Beam_Data[0]:
				print("Please enter distance between 0 - L!")
				continue
			elif DW_1 >= DW_2:
				print("DW_2 must be grater than DW_1!")
				continue

			Magnitude = W
			Converted_Load = W * (DW_2 - DW_1)
			Centroid = (DW_2 + DW_1) / 2
			Load_Data.append("Uniformly Distributed Load")
			Load_Data.append(Magnitude)
			Load_Data.append(DW_1)
			Load_Data.append(DW_2)
			Load_Data.append(Centroid)
			Load_Data.append(Converted_Load)
			Unified_Load_Structure.append(Load_Data)
			Load_Data = []
			print("--> Uniformly Distributed Load was successfully added to the beam!")
			break

		except ValueError:
			print("Please enter a numeric value!")

def TR_input():
	global Unified_Load_Structure, Load_Data, SS_Beam_Data
	while True:
		try:
			print("\n--> Triangular Load")
			T_1 = float(input("Enter triangular load in Left part (T_1, KN): "))
			T_2 = float(input("Enter triangular load in rigth part (T_2, KN): "))
			if T_1 < 0 or T_2 < 0:
				print("Please enter positive triangular load!")
				continue
			elif T_1 == T_2:
				print("Load at both ends should not be the same!")
				continue
			elif T_1 != 0 and T_2 != 0:
				print("One of the loads should be zero!")
				continue

			DT_1 = float(input("Enter the start position of (T_1) from the left (m): "))
			DT_2 = float(input("Enter the end position of (T_2) from the left (m): "))
			if DT_1 < 0 or DT_2 < 0 or DT_1 > SS_Beam_Data[0] or DT_2 > SS_Beam_Data[0]:
				print("Please enter distance between 0 - L!")
				continue
			elif DT_1 >= DT_2:
				print("DT_2 must be grater than DT_1!")
				continue
			
			#Increasing Triangular Load
			if T_2 > T_1:
				Magnitude = T_2
				Converted_Load = (1 / 2) * T_2 * (DT_2 - DT_1)
				Centroid = ((2 / 3) * (DT_2 - DT_1)) + DT_1
				Load_Data.append("Increasing Triangular Load")
				Load_Data.append(Magnitude)
				Load_Data.append(DT_1)
				Load_Data.append(DT_2)
				Load_Data.append(Centroid)
				Load_Data.append(Converted_Load)
				Unified_Load_Structure.append(Load_Data)
				Load_Data = []
				print("--> Triangular Load was successfully added to the beam!")
				break

			#Decreasing Triangular Load
			elif T_1 > T_2:
				Magnitude = T_1
				Converted_Load = (1 / 2) * T_1 * (DT_2 - DT_1)
				Centroid = ((1 / 3) * (DT_2 - DT_1)) + DT_1
				Load_Data.append("Decreasing Triangular Load")
				Load_Data.append(Magnitude)
				Load_Data.append(DT_1)
				Load_Data.append(DT_2)
				Load_Data.append(Centroid)
				Load_Data.append(Converted_Load)
				Unified_Load_Structure.append(Load_Data)
				Load_Data = []
				print("--> Triangular Load was successfully added to the beam!")				
				break

		except ValueError:
			print("Please enter a numeric value!")

def moment_input():
	global Unified_Load_Structure, Load_Data, SS_Beam_Data
	while True:
		try:
			print("\n--> Moment Load")
			Moment_value = float(input("Enter absolute value of moment (KN-m): "))
			if Moment_value <= 0:
				print("Please enter a positive moment value!")
				continue
			Location = float(input("Enter the location of the moment from the left (m): "))
			if Location < 0 or Location > SS_Beam_Data[0]:
				print("Please enter location between 0 - L!")
				continue
			Direction = input("Enter moment direction:\n'1' - Clockwise (+)\n'2' - Counterclockwise (-)\nResponse --> ")
			if not Direction:
				print("Please choose between 1 - 2!")
				continue
			elif Direction == '1':
				Load_Data.append("Moment Load")
				Load_Data.append(Moment_value)
				Load_Data.append("CW")
				Load_Data.append(Location)
				Unified_Load_Structure.append(Load_Data)
				Load_Data = []
				print("--> Moment Load was successfully added to the beam!")
				break
			elif Direction == '2':
				Load_Data.append("Moment Load")
				Load_Data.append(Moment_value)
				Load_Data.append("CCW")
				Load_Data.append(Location)
				Unified_Load_Structure.append(Load_Data)
				Load_Data = []
				print("--> Moment Load was successfully added to the beam!")
				break
			else:
				print("Please choose between 1 - 2!")
				continue

		except ValueError:
			print("Please enter a numeric value!")

def handle_multiple_loads():
	while True:
		try:
			print("\nPART-3: Input of multiple applied loads in the beam")
			no_loads = int(input("Enter number of applied loads and moments: "))
			if no_loads <= 0:
				print("Please enter a positive number of loads and moments!")
				continue

			i = 1
			while i <= no_loads:
				print(f"\n--> Load No.: {i}")
				print("Choose the type of load: ")
				print("'1' - Point Load\n'2' - UDL\n'3' - Triangular Load\n'4' - Moment")
				type = input("Response --> ")
				if type == '1':
					point_load_input()
					i += 1
				elif type == '2':
					UDL_input()
					i += 1
				elif type == '3':
					TR_input()
					i += 1
				elif type == '4':
					moment_input()
					i += 1
				else:
					print("Please choose between 1 - 3!")
					continue
			break

		except ValueError:
			print("Please enter numeric value!")

def simply_supported_reaction():
	global Unified_Load_Structure, SS_Beam_Data, Load_Data
	print("\nPART-5: Calculation of Reactions")
	print("--> Calculating reactions....")
	time.sleep(2.5)
	Moment_Sum = 0
	Shear_Sum = 0
	for n in Unified_Load_Structure:
		if n[0] == "Moment":
			if n[2] == "CW":
				Moment_Sum -= n[1]
			elif n[2] == "CCW":
				Moment_Sum += n[1]
		else:
			Moment_Sum += n[5] * (SS_Beam_Data[2] - n[4])
			Shear_Sum += n[5]
	R_1 = Moment_Sum / (SS_Beam_Data[2] - SS_Beam_Data[1])
	R_2 = Shear_Sum - R_1

	SS_Beam_Data.append(R_1)
	SS_Beam_Data.append(R_2)

	Load_Data.append("Reaction_1")
	Load_Data.append(R_1)
	Load_Data.append(SS_Beam_Data[1])
	Unified_Load_Structure.append(Load_Data)
	Load_Data = []

	Load_Data.append("Reaction_2")
	Load_Data.append(R_2)
	Load_Data.append(SS_Beam_Data[2])
	Unified_Load_Structure.append(Load_Data)
	Load_Data = []
	print("--> Reactions was calculated successfully!")

def shear_moment_calculation():
	global Unified_Load_Structure, SS_Beam_Data, Distance, Shear, Moment
	print("\nPART-6: Calculating Shear and Moment Diagram")
	print("--> Calculating....")
	time.sleep(2)
	print("\n----Shear and Moment Diagram----")
	X = 1e-100
	while X <= SS_Beam_Data[0] + 1e-2:
		V = 0
		M = 0
		for i in Unified_Load_Structure:
			#Reaction 1
			if i[0] == "Reaction_1":
				if X < i[2]:
					continue
				elif i[2] <= X:
					V += i[1]
					M += i[1] * (X - i[2])
			#Reaction 2
			elif i[0] == "Reaction_2":
				if X < i[2]:
					continue
				elif i[2] <= X:
					V += i[1]
					M += i[1] * (X - i[2])
			#Point Load
			elif i[0] == "Point Load":
				if X < i[2]:
					continue
				elif i[2] <= X:
					V -= i[1]
					M -= i[1] * (X - i[2])
			#Uniformly Distributed Load
			elif i[0] == "Uniformly Distributed Load":
				if X < i[2]:
					continue
				elif i[2] <= X < i[3]:
					Area = i[1] * (X - i[2])
					Centroid = (X + i[2]) / 2
					V -= Area
					M -= (Area * (X - Centroid))
				elif i[3] <= X:
					Area = i[1] * (i[3] - i[2])
					Centroid = ((i[2] + i[3]) / 2)
					V -= Area
					M -= Area * (X - Centroid)
			#Increasing Triangular Load
			elif i[0] == "Increasing Triangular Load":
				if X < i[2]:
					continue
				elif i[2] <= X < i[3]:
					Y = ((i[1] * (X - i[2])) / (i[3] - i[2]))
					Area = (1 / 2) * Y * (X - i[2])
					Centroid = (2 / 3) * (X - i[2])
					V -= Area
					M -= Area * (X - (i[2] + Centroid))
				elif i[3] <= X:
					Area = (1 / 2) * i[1] * (i[3] - i[2])
					V -= Area
					M -= Area * (X - i[4])
			#Decreasing Triangular Load
			elif i[0] == "Decreasing Triangular Load":
				if X < i[2]:
					continue
				elif i[2] <= X < i[3]:
					Y = ((i[1] * (i[3] - X)) / (i[3] - i[2]))
					A_rect = Y * (X - i[2])
					A_tri = (1 / 2) * (i[1] - Y) * (X - i[2])
					Cen_rect = (X + i[2]) / 2
					Cen_tri = (1 / 3) * (X - i[2])
					V -= (A_rect + A_tri)
					M -= ((A_rect * (X - Cen_rect)) + (A_tri * (X - (i[2] + Cen_tri))))
				elif i[3] <= X:
					Area = (1 / 2) * i[1] * (i[3] - i[2])
					V -= Area
					M -= Area * (X - i[4])
			elif i[0] == "Moment":
				if X < i[3]:
					continue
				elif i[3] <= X:
					if i[2] == "CW":
						M += i[1]
					elif i[2] == "CCW":
						M -= i[1]
			elif i[0] == "Moment_Reaction":
				if X < i[2]:
					continue
				elif i[2] <= X:
					if i[3] == "CCW":
						M -= i[1]
					elif i[3] == "CW":
						M += i[1]
					
		Distance.append(X)
		Shear.append(V)
		Moment.append(M)	
		print(f"At X = {X}, V = {V:.03f}KN, M = {M:.03f}KN-m")		
		X += SS_Beam_Data[0] / 500
		X = round(X, 4)
	print("--> Shear and Moment was calculated successfully!")

def plotting_graph():
	print("\nPART-9: Generating Graph for Shear and Moment Diagram")
	print("--> Generating graph....")
	time.sleep(1.5)
	# Create figure with 2 rows, 1 column (shared X-axis)
	fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
	# --- SHEAR DIAGRAM (TOP) ---
	ax1.plot(Distance, Shear, color='red')
	ax1.set_ylabel("Shear (kN)")
	ax1.set_title("Shear Force Diagram")
	ax1.axhline(0, color='black')
	ax1.grid(True)
	# --- MOMENT DIAGRAM (BOTTOM) ---
	ax2.plot(Distance, Moment, color='red')
	ax2.set_ylabel("Moment (kN·m)")
	ax2.set_xlabel("Beam Length (m)")
	ax2.set_title("Bending Moment Diagram")
	ax2.axhline(0, color='black')
	ax2.grid(True)
	# Layout adjustment
	plt.tight_layout()
	# Show
	plt.show()



#Main Interval
while True:
	try:
		print("\n---- Beam Analysis Tool ----")

		#Choosing Type of Support and Input of Beam Length
		print("\nPART-1: Choosing the type of support")
		print("Choose the type of support in the beam: ")
		print("'1' - Simply Supported Beam\n'2' - Fixed Support Beam")
		support_option = input("Response --> ")
		if support_option == '1':
			simply_supported_input()
		elif support_option == '2':
			fixed_support_input()
		else:
			print("Please choose between 1 - 2!")
			continue
		
		#Input of Multiple Loads
		handle_multiple_loads()

		#Display of Given Beam Parameters and Applied Loads
		print("\nPART-4: Display of Given Beam Parameters and Applied Loads")
		print("--> Beam Parameters")
		if support_option == '1':
			print(f"Beam Length: {SS_Beam_Data[0]}m")
			print(f"Distance of R1: {SS_Beam_Data[1]}m")
			print(f"Distance of R2: {SS_Beam_Data[2]}m")
		elif support_option == '2':
			print(f"Beam Length: {SS_Beam_Data[0]}m")
		print("\n--> Applied Loads")
		for r in Unified_Load_Structure:
			print(f"Type of Load: {r[0]}")
			print(f"Magnitude: {r[1]}KN")
			print(f"Start Position: {r[2]}m")
			print(f"End Position: {r[3]}m")
			print(f"Converted Load: {r[5]}KN\n")
		time.sleep(3)

		#Calculation of Reactions
		if support_option == '1':
			simply_supported_reaction()
		elif support_option == '2':
			print("PART-3.5: Choosing location of fixed support in the beam")
			print("Choose the location of the fixed support.\n'1' - Left Fixed Support\n'2' - Right Fixed SUpport")
			fixed = input("Response --> ")
			if fixed == '1':
				left_fixed_reaction()
			elif fixed == '2':
				right_fixed_reaction()
			else:
				print("Please choose between 1 - 2!")
				continue

		#Shear and Moment in each point
		shear_moment_calculation()

		#Display of Reactions
		print("\nPART-7: Display of Reactions")
		if support_option == '1':
			print(f"R1 (Left reaction): {SS_Beam_Data[3]:.03f}KN")
			print(f"R2 (Right reaction): {SS_Beam_Data[4]:.03f}KN")
		elif support_option == '2':
			print(f"R1 (Left reaction): {SS_Beam_Data[1]:.03f}KN")
			print(f"R2 (Right reaction): {SS_Beam_Data[2]:.03f}KN")
			print(f"Moment reaction: {SS_Beam_Data[3]:.03f}KN-m")

		#Max Shear and Max Moment
		print("\nPART-8: Display of Maximum and Minimum of Shear Force and Bending Moment")
		Plus_Max_Shear = max(Shear)
		Minus_Max_Shear = min(Shear)
		Plus_Max_Moment = max(Moment)
		Minus_Max_Moment = min(Moment)
		print(f"+Vmax = {Plus_Max_Shear:.03f}KN")
		print(f"-Vmax = {Minus_Max_Shear:.03f}KN")
		print(f"+Mmax = {Plus_Max_Moment:.03f}KN-m")
		print(f"-Mmax = {Minus_Max_Moment:.03f}KN-m")

		#Plotting Graphs
		plotting_graph()

		Unified_Load_Structure = []
		SS_Beam_Data = []
		Distance = []
		Shear = []
		Moment = []

		print("\nUse again?\nEnter anything to use again.\nEnter 'q' to exit.")
		again = input("Response --> ").lower()
		if again == 'q':
			print("Thank you for using the program.")
			break
				
	except ValueError:
		print("Please enter a numeric input!")