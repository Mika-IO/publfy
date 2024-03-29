span = """"""
number_from_whatsapp_group = span.split(",")
formated_numbers = [number.replace(" ", "").replace("-", "").replace("\n", "") for number in number_from_whatsapp_group]
