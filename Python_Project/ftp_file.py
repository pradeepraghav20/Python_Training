from ftplib import FTP


def download_file_from_ftp(server, username, password, remote_filepath, local_filepath):
    ftp = FTP(server)
    ftp.login(username, password)

    # Change to the directory containing the file
    ftp.cwd(remote_filepath.rsplit('/', 1)[0])

    # Download the file
    with open(local_filepath, 'wb') as file:
        ftp.retrbinary('RETR ' + remote_filepath.rsplit('/', 1)[1], file.write)

    ftp.quit()
    print(f"File downloaded successfully to {local_filepath}")


# Example usage
server = 'ftp.example.com'
username = 'your_username'
password = 'your_password'
remote_filepath = '/path/to/remote/file.txt'
local_filepath = 'local_file.txt'

download_file_from_ftp(server, username, password, remote_filepath, local_filepath)
