# Run this if you want to have this as a service
import os

def main():
	print("Setting the Service")
	os.system("cp mobile_data.service /etc/systemd/system")
	os.system("systemctl enable mobile_data.service")
	os.system("systemctl start mobile_data.service")

	print("done")
if __name__ == '__main__':
	main()