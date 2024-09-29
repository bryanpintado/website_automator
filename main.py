import sys 
import webbrowser

tasks = {'leet_code': ['https://neetcode.io/practice', 'https://www.youtube.com'],
         'school': ['https://rutgers.instructure.com/courses', 'https://my.rutgers.edu/uxp/']
}

def openURL ():
    for i in x:
        webbrowser.open(i)
      
if __name__ == '__main__':    
    try:
        task = sys.argv[1]
        x = tasks[task]
        openURL()
    except:
        print("Task Not Found")