from datetime import datetime

format_string_pattern = 'mm/dd/yyyy'

class MoveDateValidator():

    def __init__(self, datestring):
        self.now = datetime.utcnow()
        self.month = datestring[:2]
        self.day = datestring[3:5]
        self.year = datestring[6:]
    
    def validate_move_date(self):
        move_date = datetime(int(self.year), int(self.month), int(self.day))
        return move_date > self.now

    @staticmethod
    def validate_date_string(datestring):
        try:
            datetime.strptime(datestring, '%m/%d/%Y')
            return True
        except ValueError:
            return False
        
