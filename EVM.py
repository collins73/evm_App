"""EARNED VALUE MANAGEMENT (EVM) CALCULATOR APP """

"""
This simple program will perform Earned Value Management (EVM) analysis calculations for controlling/monitoring
cost when managing projects. All the EVM formulas will be defined below. This application also assumes that the
planned % completed will always be given as a percentage. If while conducting EVM analysis and the
planned % completed is not provided "explicitly", then take the now(current time) and divide by the
overall project duration.

"""

# User to provide budget expenditures and actual project cost
BAC_request = int(
    input("Enter budget at completion $")
)
"""
BAC is the Budget At Completion or original budget of the project
"""
AC_request = int(input("Enter actual cost $"))
"""
AC is the Actual Cost or the amount of money already spent on the project
"""
# User to provide the percent complete for both planned activities and the actual percent complete for work done
planned_percent_complete = float(input("Enter Planned % Completed "))
actual_percent_complete = float(input("Enter the Actual % Completed "))

# Compute the Planned and Earned Value estimates respectfully
PV = planned_percent_complete * BAC_request
"""
Amount of money worth of work that we should have been done on the project. 
"""
EV = actual_percent_complete * BAC_request
"""
Amount of money worth of work you actually did on the project. 
"""


print("The Planned value is: $" + str(PV))
print("The Earned value is: $" + str(EV))


def costVariance(EV1):
    """
    The difference between the work done and money spent. This value
    should be positive for under budget. Negative values indicate
    under budget.
    """
    result = EV - AC_request
    if result < 0:
        print("Project is over budget")
    else:
        print("Project is under budget")

    return "The cost variance is: $" + str(result)


print(costVariance(EV))


def costPerformanceIndex(CPI):
    """
    The rate of how we are spending to actually earning on
    the project. The value should be 1 and over for projects
    under budget.
    """
    CPI = EV / AC_request
    EAC = BAC_request / CPI
    """
    Forcasting the total cost of the project at the end
    based on the current spending rate of the project. 
    """
    print("The Estimate at Completion is: $" + str(round(EAC, 2)))
    ETC = EAC - AC_request
    """
    Forcasting the amount that will be needed to complete the current
    project based on the current performance.
    """
    print("The Estimate to Completion is: $" + str(round(ETC, 2)))
    VAC = BAC_request - EAC
    """
    The difference between the original budget and new forecasted budget. This value should
    be positive for projects that may end at or under budget.
    """
    print("The Variance at Completion is: $" + str(round(VAC)))
    """The performance that needs to be met to finish the project within the budget"""
    TCPI = (BAC_request - EV) / (BAC_request - AC_request)
    """
    The performance that needs to be met to finish the project within the budget. 
    """
    print("The To-Complete Performance Index is: " + str(round(TCPI, 2)))
    if CPI >= 1:
        print("Project is under budget")
    else:
        print("Project is over budget")
    if AC_request == 0:
        raise ZeroDivisionError("Opps, division by zero detected")
    return round(CPI, 1)


print("The Cost Performance Index is: " + str(costPerformanceIndex(EV / AC_request)))


def scheduleVariance(EV1, PV1):
    """
    The difference between the amount of work we should have done vs. the amount actually done.
     This value should be positive for ahead of schedule. Negative values indicate
     behind schedule.
    """
    answer2 = EV - PV
    if answer2 < 0:
        print("Project is behind schedule")
    else:
        print("Project is ahead of schedule")
    return "The schedule variance is: $" + str(answer2)


print(scheduleVariance(EV, PV))


def schedulePerformanceIndex(EV1, PV1):
    """
    The rate of how we are meeting the project schedule. This value
    should be 1 and over for a project to be ahead of schedule.
    """
    answer3 = EV / PV
    if answer3 >= 1:
        print("Project is ahead of schedule")
    else:
        print("Project is behind schedule")
    if PV == 0:
        raise ZeroDivisionError("Opps, division by zero detected")
    return "The schedule performance index is: " + str(round(answer3, 1))
    # return answer3


print(schedulePerformanceIndex(EV, PV))
