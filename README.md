# StatusV3

This is a Python script that performs a fast mass port scan on a list of domains. It checks the status of each domain and provides information about the response codes. The script supports custom ports and allows you to specify the timeout duration and the number of threads to use.

## Usage

1. Clone the repository:

  git clone https://github.com/your-username/StatusV3.git
   
2. Navigate to the project directory:

  cd fast-mass-port-scanner
   
3. Install the required dependencies:

  pip install -r requirements.txt
   
4. Run the script:

  python scanner.py
   

5. Follow the prompts to provide the necessary inputs:

   - Enter the path to your list of domains.
   - Choose whether to check a custom port.
   - Specify the port number and protocol if applicable.
   - Set the timeout duration.

6. The script will start scanning the domains using multiple threads for faster execution.

## Example

Here's an example of how the script can be used:

$ python scanner.py

Your list Domain Please?: domains.txt

Are We checking A custom Port? (yes or no): yes

What port are you looking at today?: 8080

Is this HTTP or HTTPS?: HTTP

How many seconds timeout do you wish to use?: 5

How many threads do you wish to use?: 10
