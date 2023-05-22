from RPA.Browser.Selenium import Selenium
import constants
import time
import threading
br = Selenium()


class Robot:
    def __init__(self, name,loading):
        self.name = name
        self.loading = loading

    def say_hello(self,SCIENTISTS):
        print("Hello, my name is " + self.name + "\n" + constants.dashes + "\n" + constants.intro_text + str(SCIENTISTS))
        print(constants.dashes)

    def loading_animation(self):
        j = 0
        # Loading animation while the browser closes 
        while(self.loading):
            print(constants.bar[j % len(constants.bar)], end="\r")
            time.sleep(.2)
            j += 1

    def open_webpage(self, webpage,scientist):
        provided_name = scientist.split(" ")
        br.open_available_browser(webpage)
        i = 1
        max_iterations = 5
        # Check each <p> tag at top of page for the actual First paragraph
        while(i < max_iterations):
            paragraph = br.get_text("class:mw-parser-output p:nth-of-type("+str(i)+")")
            words = paragraph.split()
            if(words):
                name = words[0]
                # skip official title
                if(name == constants.title): name = words[1]
                # Return the first paragraph from the wiki
                if(name == provided_name[0]):
                    self.loading = True
                    t = threading.Thread(target=self.loading_animation)
                    t.start()
                    br.close_all_browsers()
                    self.loading = False
                    t.join()        
                    return paragraph
                
            i += 1

        return None
        
        
