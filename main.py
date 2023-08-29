#Title: Car breakdown solution program
#Author: Daniel Mukenya Nyongesa
#License: MIT
#Date: 29/08/23
#Inspiration: Driving experience and car lover.
#Don't steal hahaha kidding, give me my credits. Love. In a bit

import sys
import mercedes
import volks
import mobius
import honda
import mazda
import subaru

print("\t\t\t\t\t\t\t\tWELCOME TO FRADS CAR SOLUTIONS.")
print("\t\t\t\tVery warm welcome, we solve car problems before further actions.")
print("Kindly select the car model from the list below:")
print(f"1. Mobius\n"
      f"2. Toyota\n"
      f"3. Honda\n"
      f"4. Mazda\n"
      f"5. Subaru\n"
      f"6. Volkswagen\n"
      f"7. Mercedes\n"
      f"8. BMW\n"
      f"9. Exit\n")

choice = int(input("Which model: "))

def mobius():
      print(f"\t1.Quality control issues\n"
            f"\t2.Supply chain challenges\n"
            f"\t3.Rough road durability\n"
            f"\t4.Maintenance and servicing\n"
            f"\t5.Limited model range\n"
            f"\t6.Resale value\n"
            f"\t7.Perception & brand awareness\n"
            f"\t8.Financing & affordability\n"
            f"\t9.Regulatory & compliance issues\n"
            f"\t10.Competition\n")

def toyota():
      print(f"\t1.Brake problems\n"
            f"\t2.Suspension issues\n"
            f"\t3.Faulty water pumps\n"
            f"\t4.Fuel pump failures\n"
            f"\t5.Oil sludge in engines\n"
            f"\t6.Poor air conditioning\n")

def honda():
      print(f"\t1.Failing transmission\n"
            f"\t2.Engine issues\n"
            f"\t3.Defective airbags\n"
            f"\t4.Power steering Hose Failure\n"
            f"\t5.Car moves due to ignition interlock fault\n"
            f"\t6.Risk of automatic transmission locking up\n"
            f"\t7.Automatic transmission short circuiting\n"
            f"\t8.Fuel pump abrupt power loss\n")

def mazda():
      print(f"\t1.Clutch issues(Manual)\n"
            f"\t2.Untrustworthy engines\n"
            f"\t3.Brake booster issues\n"
            f"\t4.Melting Dashboards\n")

def subaru():
      print(f"\t1.Fuel pump failure\n"
            f"\t2.Oxygen sensor problems\n"
            f"\t3.Blown head gaskets\n"
            f"\t4.Oil leaks\n"
            f"\t5.Battery draining rapidly\n"
            f"\t6.Unintended acceleration\n"
            f"\t7.Crack windshields\n"
            f"\t8.Subaru starlink problems\n")

def volkswagen():
      print(f"\t1.Overactive check engine light\n"
            f"\t2.Oil problems\n"
            f"\t3.Coolant leaks\n"
            f"\t4.Vehicle overheating\n"
            f"\t5.Suspension issues\n")

def mercedes():
      print(f"\t1.Engine mounts failure\n"
            f"\t2.Engine misfires\n"
            f"\t3.Oil & Differential leaks\n"
            f"\t4.Air suspension failure\n"
            f"\t5.Transmission issues\n"
            f"\t6.Rusts easily & rapidly\n"
            f"\t7.Get ahead in the mercedes benz game\n")

def bmw():
      print(f"\t1.Oil leaks\n"
            f"\t2.Cooling system failure\n"
            f"\t3.Shaking steering wheel\n"
            f"\t4.Tail lamp problems\n")

if choice == 1:
      mobius()
      print(f"Want a guideline to fix each?\n"
            f"1. Yes\n"
            f"2. No\n")
      solulu = int(input("Choice: "))
      if solulu == 1:
            print(f"**** MOBIUS**** "
                  f"1. Quality control issuses - ")

      else:
            sys.exit()

if choice == 2:
      toyota()
      print(f"Want a guideline to fix each?\n"
            f"1. Yes\n"
            f"2. No\n")
      solulu = int(input("Choice: "))
      if solulu == 1:
            print(f"\t\t\t\t\t*** TOYOTA *** \n"
                  f"\t1. Brake problems :- \n\n"
                  f"Listen for unusual noises such as grinding, squeaking, or squealing when braking.\n"
                  f"Pay attention to any changes in braking performance, such as longer stopping distances or a soft brake pedal.\n"
                  f"Check for warning lights on the dashboard, like the ABS (Anti-lock Braking System) light\n"
                  f"Visually inspect the brake components, including brake pads, rotors, calipers, and brake lines.\n"
                  f"Look for signs of wear, damage, or corrosion.\n"
                  f"Check for any leaks around the brake lines and calipers.\n"
                  f"Check the brake fluid level in the master cylinder reservoir.\n"
                  f"Ensure that the brake fluid is clear and within the recommended level.\n"
                  f"If the fluid is dark or contaminated, it might need to be flushed and replaced.\n"
                  f"Measure the brake pad thickness. If the pads are worn beyond the recommended thickness, they need replacement.\n"
                  f"Inspect the brake rotors for uneven wear, scoring, or grooves. Resurfacing or replacement might be necessary.\n"
                  f"Check the calipers for proper operation. Ensure they are not sticking or causing uneven pressure on the brake pads.\n"
                  f"If a caliper is malfunctioning, it might need to be rebuilt or replaced.\n"
                  f"Examine the brake lines for any signs of leakage, corrosion, or damage.\n"
                  f"Leaking brake lines can result in loss of brake fluid and reduced braking efficiency.\n"
                  f"If the ABS light is on, use a diagnostic scanner to retrieve error codes from the ABS module.\n"
                  f"Address the specific issues indicated by the codes. This might involve repairing or replacing ABS sensors, modules, or related components.\n"
                  f"Clean the wheel speed sensors if they are covered in dirt or debris, as this can affect their performance.\n"
                  f"Check for damaged or malfunctioning sensors and replace them if needed.\n"
                  f"If you're unsure about diagnosing or fixing the issue yourself, it's recommended to take your Toyota to a certified mechanic or dealership.\n"
                  f"They have the expertise and specialized tools to diagnose and repair brake-related problems accurately.\n"
                  f"Follow the recommended brake maintenance schedule outlined in your Toyota's owner's manual.\n"
                  f"Regularly inspect and replace brake pads and rotors according to the manufacturer's guidelines.\n"
                  f"Use high-quality brake components that meet or exceed OEM specifications.\n\n"
                  f"\t2. Suspension issues:-\n\n"
                  f"Pay attention to any unusual noises while driving, such as clunking, rattling, or squeaking sounds.\n"
                  f"Observe changes in the vehicle's handling, such as excessive bouncing, drifting, or uneven tire wear.\n"
                  f"Check for uneven or abnormal tire wear patterns.\n"
                  f"Inspect the suspension components, including shock absorbers/struts, springs, control arms, bushings, and sway bar links.\n"
                  f"Look for signs of damage, corrosion, leaks, or wear on these components.\n"
                  f"Bounce each corner of the vehicle and observe how it responds. Excessive bouncing or a lack of rebound control may indicate worn shock absorbers or struts.\n"
                  f"Check for oil leaks around the shock absorber/strut body.\n"
                  f"Inspect the springs for signs of damage or sagging.\n"
                  f"Uneven ride height or a noticeably lower corner of the vehicle could indicate a broken or worn spring.\n"
                  f"Look for worn or damaged control arm bushings.\n"
                  f"Inspect control arms for signs of bending, rust, or other damage.\n"
                  f"Check for any play or looseness in the sway bar links.\n"
                  f"Worn or broken sway bar links can result in handling issues and noise.\n"
                  f"An incorrect wheel alignment can lead to uneven tire wear and handling problems. Have the alignment checked by a professional.\n"
                  f"If you're not confident in diagnosing or repairing suspension issues, take your Toyota to a certified mechanic or dealership.\n"
                  f"They can perform a comprehensive inspection, identify the specific problem, and recommend the appropriate repairs.\n"
                  f"Based on the diagnosis, replace any damaged or worn suspension components with high-quality parts that meet or exceed OEM specifications.\n"
                  f"Consider replacing components in pairs (e.g., both front struts) to maintain balanced suspension performance.\n"
                  f"Follow the manufacturer's recommended maintenance schedule for suspension components.\n"
                  f"Lubricate and inspect components like bushings and joints as needed.\n"
                  f"f you're interested in improving your Toyota's suspension performance, consider upgrading to aftermarket suspension components or kits.\n"
                  f"Make sure any modifications are compatible with your vehicle and driving needs.\n"
                  f"After repairs or replacements, take your Toyota for a test drive to ensure that the suspension issues are resolved.\n"
                  f"Pay attention to handling, ride comfort, and any remaining abnormal noises.\n\n"
                  f"\t3. Faulty water pumps:- \n\n"
                  f"Observe the engine temperature gauge. If it's consistently running hotter than normal, it could be due to a failing water pump.\n"
                  f"Listen for unusual noises coming from the front of the engine, such as a loud whining or grinding sound.\n"
                  f"Check for coolant leaks under the vehicle or around the water pump area.\n"
                  f"Allow the engine to cool down completely before working on it.\n"
                  f"Wear appropriate safety gear, such as gloves and safety glasses.\n"
                  f"Obtain a replacement water pump that matches your Toyota's make, model, and engine.\n"
                  f"Gather tools such as wrenches, sockets, pliers, a coolant drain pan, and a gasket scraper.\n"
                  f"Place a coolant drain pan under the radiator.\n"
                  f"Open the radiator drain plug to allow the coolant to drain into the pan.\n"
                  f"Loosen and remove the drive belts that are connected to the water pump.\n"
                  f"Disconnect the hoses and any electrical connections attached to the water pump.\n"
                  f"Remove the bolts securing the water pump to the engine.\n"
                  f"Use a gasket scraper to clean the mounting surface on the engine block where the water pump attaches.\n"
                  f"Place a new gasket on the new water pump or apply a thin layer of gasket sealant to the pump side of the gasket.\n"
                  f"Position the new water pump onto the engine block and secure it with the bolts.\n"
                  f"Reconnect the hoses and electrical connections that were disconnected earlier.\n"
                  f"Ensure all connections are secure.\n"
                  f"Put the drive belts back onto their pulleys and adjust their tension according to the manufacturer's specifications.\n"
                  f"Close the radiator drain plug.\n"
                  f"Refill the cooling system with the appropriate coolant mixture recommended for your Toyota.\n"
                  f"Bleed any air from the cooling system by using the designated bleed screws or valves.\n"
                  f"Start the engine and let it run while checking for coolant leaks around the water pump area.\n"
                  f"Observe the engine temperature gauge to ensure it's operating within the normal range.\n"
                  f"If the old coolant is still in good condition, you can save and reuse it. If not, dispose of it according to local regulations.\n\n"
                  f"\t4.Fuel pump Failures:- \n\n"
                  f"Observe symptoms like engine cranking but not starting, sputtering, loss of power, or engine stalling.\n"
                  f"Listen for a lack of humming noise from the fuel tank area when the ignition is turned to the ON position.\n"
                  f"Use a fuel pressure gauge to measure fuel pressure at the fuel rail; low or no pressure can indicate a failed fuel pump.\n"
                  f"Work in a well-ventilated area and away from open flames or sparks.\n"
                  f"Disconnect the vehicle's battery to prevent electrical accidents.\n"
                  f"Obtain a replacement fuel pump that matches your Toyota's make, model, and engine.\n"
                  f"Have tools such as wrenches, sockets, pliers, a jack and jack stands, and a container for fuel drainage.\n"
                  f"Loosen the fuel cap to release pressure from the fuel system.\n"
                  f"Alternatively, you can use the fuel pressure relief valve (if available) on the fuel rail.\n"
                  f"Disconnect the negative terminal of the vehicle's battery.\n"
                  f"Use a fuel line disconnect tool to disconnect the fuel lines from the fuel pump.\n"
                  f"Place a container under the disconnected lines to catch any spilled fuel.\n"
                  f"If the fuel pump is located inside the fuel tank (common for many vehicles), you'll need to access it by removing the tank.\n"
                  f"Raise the vehicle using a jack and secure it with jack stands.\n"
                  f"Remove the fuel tank by loosening and removing the retaining straps, and carefully lower it.\n"
                  f"Carefully disconnect the electrical connectors and hoses attached to the old fuel pump.\n"
                  f"Remove the fuel pump assembly from the tank.\n"
                  f"Install the new fuel pump assembly, ensuring all connections are secure.\n"
                  f"Reattach the fuel tank and secure it with the retaining straps.\n"
                  f"Reconnect the fuel lines and electrical connectors.\n"
                  f"Raise the vehicle and remove the jack stands.\n"
                  f"Reconnect the negative terminal of the battery.\n"
                  f"Refill the fuel tank with clean and fresh fuel.\n"
                  f"Turn the ignition key to the ON position for a few seconds to allow the fuel pump to prime the system before cranking the engine.\n"
                  f"Start the engine and let it run, checking for any unusual noises or signs of leaks.\n"
                  f"Test drive the vehicle to ensure proper fuel delivery and engine performance.\n\n"
                  f"\t5. Oil sludge in engines:-  \n\n"
                  f"Signs of oil sludge include poor engine performance, reduced fuel efficiency, engine knocking, and increased oil consumption.\n"
                  f"Drain the existing oil and replace it with fresh, high-quality engine oil. Also, replace the oil filter. Use the oil viscosity recommended in your Toyota's owner's manual.\n"
                  f"Some mechanics might recommend an engine flush to help remove the sludge.\n"
                  f" engine cleaning additives available that can help break down and dislodge sludge deposits.\n"
                  f"Consistently follow your Toyota's recommended oil change intervals using the appropriate oil type. Regular oil changes can prevent the buildup of sludge in the first place.\n"
                  f"The Positive Crankcase Ventilation (PCV) system is responsible for removing harmful gases from the engine. A malfunctioning PCV system can contribute to oil sludge buildup. Check and replace the PCV valve if necessary.\n"
                  f"The breather system allows the engine to release pressure. If this system is clogged or malfunctioning, it can lead to sludge formation. Make sure the breather system is clean and functioning properly.\n"
                  f"Overheating can accelerate sludge formation. Ensure your Toyota's cooling system is working correctly, and address any overheating issues promptly.\n"
                  f"Regular maintenance, including checking and replacing worn components, can prevent various engine issues, \n"
                  f"f the sludge buildup is severe, it's best to consult a professional mechanic. \n\n"
                  f"\t6.Poor air conditioning:-  \n\n"
                  f" Low refrigerant levels can result in reduced cooling efficiency. If the refrigerant is low, it could indicate a leak in the system\n"
                  f"AC system leaks can be a common cause of poor cooling performance. A professional mechanic can use specialized equipment to detect leaks and address them accordingly.\n"
                  f"The condenser is responsible for releasing heat from the refrigerant. If it's obstructed by debris or damaged, it can affect cooling performance. Inspect the condenser for any visible damage or obstructions.\n"
                  f"The AC compressor is the heart of the system. If it's not functioning properly, the AC won't cool effectively. Listen for any unusual noises coming from the compressor, and have it inspected by a professional if necessary."
                  f"The AC system relies on belts and pulleys to operate. Worn or damaged belts can impact the system's efficiency. Have the belts and pulleys checked during routine maintenance.\n"
                  f"A clogged or dirty cabin air filter can restrict airflow, leading to reduced cooling performance. Replace the cabin air filter according to your vehicle's recommended maintenance schedule.\n"
                  f"Make sure there are no obstructions blocking the vents both inside the cabin and in the engine compartment. Obstructed vents can restrict airflow, affecting cooling.\n"
                  f"The AC system relies on electrical components to function. If there's an issue with the electrical system, it can affect AC performance. A professional mechanic can diagnose and repair any electrical issues.\n"
                  f"The cooling fan helps dissipate heat from the AC system. If the cooling fan isn't working properly, it can lead to inadequate cooling. Check if the cooling fan is turning on as it should.\n"
                  f"If you're unable to identify the problem or if the issue is more complex, it's recommended to seek help from a qualified mechanic. \n\n"
                  f"\t\t\t****************Thank you. Toyota got you*************************\n\n")

      else:
            print("\t\tClosing the program.!!!!!")
            sys.exit()
if choice == 3:
      honda()
if choice == 4:
      mazda()
if choice == 5:
      subaru()
if choice == 6:
      volkswagen()
if choice == 7:
      mercedes()
if choice == 8:
      bmw()
if choice == 9:
      print("Exiting the program...........!!")
      sys.exit()



