class Trace:
    def __init__(self, swf_file, xml_file, number_of_experiments):
        self.swf = swf_file
        self.xml = xml_file
        self.number_of_experiments = number_of_experiments

class ANL(Trace):
    def __init__(self):
        swf_file = "swfs/ANL-Intrepid-2009-1.swf"
        xml_file = "xmls/deployment_anl.xml"
        number_of_experiments = 15
        
        super().__init__(swf_file, xml_file, number_of_experiments)