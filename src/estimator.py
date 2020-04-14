import math
input = {
    'region': {
        "name" : 'Africa',
        'avgAge' : 19.7,
        'avgDailyIncomeInUSD' : 5,
        'avgDailyIncomePopulation' : 0.71
    },
    'periodTypes' : 'days',
    'timeToElapse' : 58,
    'reportedCases' : 674,
    'population' : 66622705,
    'totalHospitalBeds' : 1380614 
}

def get_currently_infected_people(reportedCases):
    return reportedCases * 10


def get_currently_infected_people_severe(reportedCases):
    return reportedCases * 50
 

def getInfectionsByRequestedTime(currentlyInfected, duration):
    factor = math.ceil(duration/3)
    return currentlyInfected * (pow(2, factor))

def get_severe_cases_by_requested_time(infectionsByRequestedTime):
    return 0.15 * infectionsByRequestedTime


def get_hospital_beds_by_requested_time(severeCasesByRequestedTime, totalHospitalBeds):
    beds_availability = math.ceil(0.35 * totalHospitalBeds)
    number_of_beds_available = beds_availability - severeCasesByRequestedTime
    return number_of_beds_available

def get_cases_for_ICU_by_requested_time(infectionsByRequestedTime):
    return math.ceil(0.05 * infectionsByRequestedTime)

def get_casesForVentilatorsByRequestedTime(infectionsByRequestedTime):
    return math.ceil(0.02 * infectionsByRequestedTime)


def get_dollarsInFlight(infectionsByRequestedTime, duration_in_days, avgDailyIncomeInUSD):
    return infectionsByRequestedTime * duration_in_days * avgDailyIncomeInUSD



def estimator(data):
    currentlyInfectedPeople = get_currently_infected_people(data.get('reportedCases'))
    currentlyInfectedPeopleSevere = get_currently_infected_people_severe(data.get('reportedCases'))
    output = {
        'data' : data,
        'impact' :{
            'currentlyInfectedPeople' : currentlyInfectedPeople,
            'infectionsByRequestedTime' : getInfectionsByRequestedTime(currentlyInfectedPeople, (data.get('timeToElapse')/24)),
            'severeCasesByRequestedTime' : get_severe_cases_by_requested_time(getInfectionsByRequestedTime(currentlyInfectedPeople, (data.get('timeToElapse')/24))),
            'hospitalBedsByRequestedTime' : get_hospital_beds_by_requested_time(get_severe_cases_by_requested_time(getInfectionsByRequestedTime(currentlyInfectedPeople, (data.get('timeToElapse')/24))), data.get('totalHospitalBeds')),
            'casesForICUByRequestedTime' : get_cases_for_ICU_by_requested_time(getInfectionsByRequestedTime(currentlyInfectedPeople, (data.get('timeToElapse')/24))),
            'casesForVentilatorsByRequestedTime' : get_casesForVentilatorsByRequestedTime(getInfectionsByRequestedTime(currentlyInfectedPeople, (data.get('timeToElapse')/24))),
            'dollarsInflight' : get_dollarsInFlight(getInfectionsByRequestedTime(currentlyInfectedPeople, (data.get('timeToElapse')/24)), (math.ceil(data.get('timeToElapse')/24)),data.get('region').get('avgDailyIncomeInUSD'))
        },
        'severeImpact' : {
            'currentlyInfectedPeople' : currentlyInfectedPeopleSevere, 
            'infectionsByRequestedTime' : getInfectionsByRequestedTime(currentlyInfectedPeopleSevere, (data.get('timeToElapse')/24)),
            'severeCasesByRequestedTime' : get_severe_cases_by_requested_time(getInfectionsByRequestedTime(currentlyInfectedPeopleSevere, (data.get('timeToElapse')/24))),
            'hospitalBedsByRequestedTime' : get_hospital_beds_by_requested_time(get_severe_cases_by_requested_time(getInfectionsByRequestedTime(currentlyInfectedPeopleSevere, (data.get('timeToElapse')/24))), data.get('totalHospitalBeds')),
            'casesForICUByRequestedTime' : get_cases_for_ICU_by_requested_time(getInfectionsByRequestedTime(currentlyInfectedPeopleSevere, (data.get('timeToElapse')/24))),
            'casesForVentilatorsByRequestedTime' : get_casesForVentilatorsByRequestedTime(getInfectionsByRequestedTime(currentlyInfectedPeopleSevere, (data.get('timeToElapse')/24))),
            'dollarsInflight' : get_dollarsInFlight(getInfectionsByRequestedTime(currentlyInfectedPeopleSevere, (data.get('timeToElapse')/24)), (math.ceil(data.get('timeToElapse')/24)),data.get('region').get('avgDailyIncomeInUSD') )
        }
    }

    return output

if __name__ == '__main__':
    print(estimator(input))



