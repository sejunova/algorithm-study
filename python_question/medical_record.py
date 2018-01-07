# A hospital patient tracking system is restructuring its patient
# records. The current format is fragmented, each patient is
# represented as a list of namedtuple. Each element contains a
# different piece of information about the patient.

# Your task is to write a function that merges all of the information
# into one namedtuple, named Patient, in the order that it's provided
# to the function

# For Example,
# PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
# personal_details = PersonalDetails(date_of_birth = '06-04-1972')

# Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
# complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')

# print(MedicalRecord.merge(personal_details, complexion))

from collections import namedtuple


class MedicalRecord:

    # params varargs list of namedtuple representing the patient details.
    # Returns namedtuple, named patient containing details from all records

    @staticmethod
    def merge(*records):
        medical_records = {}
        for record in records:
            for field in record._fields:
                medical_records[field] = getattr(record, field)

        Patient = namedtuple('Patient', [attr for attr in medical_records.keys()])
        patient = Patient(**medical_records)
        return patient


PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth='06-04-1972')
Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color='Blue', hair_color='Black')
print(MedicalRecord.merge(personal_details, complexion))
