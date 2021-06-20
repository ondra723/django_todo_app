from django.forms.widgets import Input

class DatePickerWidget(Input):
    input_type = "date"

class TimePickerWidget(Input):
    input_type = "time"

    # def render(self):
    #     attrs_str = " ".join(["=".join([key, "\"" + str(value) + "\""]) for key, value in self.attrs.items()])
    #     return f'<input type="date" {attrs_str}>'


