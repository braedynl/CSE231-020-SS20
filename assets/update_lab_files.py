import zipfile
import os 

def main():

    folders = os.listdir()

    for folder in folders:
        if 'lab' in folder.lower() and '.' not in folder:
            n = int(folder[-2:])

            if n == 0:
                continue

            os.chdir(folder)

            readme_temp = open('../assets/templates/lab_info_temp.md', 'r').read().replace(':n:', str(n)).replace(':n02d:', '{:02d}'.format(n))
            readme = open('README.md', 'w+')
            print(readme_temp, file=readme)
            readme.close()

            zip_file = zipfile.ZipFile('../assets/packages/lab{:02d}_contents.zip'.format(n), 'w')
            for file_name in os.listdir():
                if file_name == 'presentation':
                    os.chdir('presentation')
                    for file_name in os.listdir():
                        zip_file.write(file_name, 'presentation/{}'.format(file_name), compress_type=zipfile.ZIP_DEFLATED)
                    os.chdir('..')
                else:
                    zip_file.write(file_name, compress_type=zipfile.ZIP_DEFLATED)

            zip_file.close()

            os.chdir('..')

if __name__ == "__main__":
    main()