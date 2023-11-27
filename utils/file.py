class file:

    def __init__(self, location, text):
            self.location = location
            self.text = text

            
    def read(location):
        with open(location) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                return line.strip()
            

    def write(location, text):
        with open(location, 'a') as f:
            f.write(text + '\n')