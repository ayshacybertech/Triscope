# Triscope
A tool for vulnerability scanning using Nmap, Gobuster, and Nikto
# Triscope

Triscope is a powerful vulnerability scanning tool that utilizes three popular open-source tools: Nmap, Gobuster, and Nikto. It offers three types of scans—Quick Scan, Basic Scan, and Full Scan—to assess the security posture of your target systems and web applications.

## Features

- **Quick Scan**: A fast scan for basic information about the target, using default Nmap scripts and port scanning.
- **Basic Scan**: Scans for common vulnerabilities using Nmap, Gobuster, and Nikto to detect open ports, directories, and web application vulnerabilities.
- **Full Scan**: Performs a comprehensive scan using all Nmap scripts, Gobuster for exhaustive directory enumeration, and Nikto for full web vulnerability scanning.

## Installation

To use Triscope, you'll need to have Nmap, Gobuster, and Nikto installed on your system.

### Dependencies

1. **Nmap**: [Nmap Download](https://nmap.org/download.html)
2. **Gobuster**: [Gobuster GitHub](https://github.com/OJ/gobuster)
3. **Nikto**: [Nikto GitHub](https://github.com/sullo/nikto)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Triscope.git
   cd Triscope
2. Install the required dependencies (Nmap, Gobuster, and Nikto) if they are not installed on your system.

## Usage

Run the tool by specifying the scan type and the target.

### Quick Scan

python triscope.py --scan quick --target <target-ip>

### Basic Scan

python triscope.py --scan basic --target <target-ip>

### Full Scan

python triscope.py --scan full --target <target-ip>

Example --
python triscope.py --scan full --target 192.168.1.1

Contributing
Contributions to improve Triscope are welcome! If you find any bugs or would like to add new features, feel free to open an issue or submit a pull request.
