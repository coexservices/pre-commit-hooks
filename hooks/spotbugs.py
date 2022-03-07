import subprocess

def main():
    status, output = subprocess.getstatusoutput('mvn spotbugs:check')
    print(output)
    return 0 if status==0 else 1

if __name__ == '__main__':
    raise SystemExit(main())