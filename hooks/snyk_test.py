import subprocess

def main():
    status, output = subprocess.getstatusoutput('snyk test --severity-threshold=high')
    print(output)
    return 0 if status==0 else 1

if __name__ == '__main__':
    raise SystemExit(main())