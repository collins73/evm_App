/* The code below will perform earned value calculations for monitoring cost and scheduling for typical projects. The user will be prompted to enter certain values
 in order to complete the formulas below. */

fun main()
{
    // Prompt user to enter project budget at completion
    println("The Budget at Completion is: ")
    var budgetAtCompletion = readLine()!!
    println("The Budget at Completion is: $${budgetAtCompletion.toDouble()}")

    // Prompt user to enter planned % complete
    println("Enter planned % complete")
    var plannedPercentComplete = readLine()!!
    println("Planned % Complete is: $plannedPercentComplete ")

    // Prompt user to enter actual % complete
    println("Enter the actual % complete")
    var actualPercentComplete = readLine()!!
    println("Actual % complete is: ${actualPercentComplete.toDouble()}")

    // Prompt user to enter actual cost for the project
    println("Enter the actual cost")
    var actualCost = readLine()!!
    println("The Actual amount of money spent is: $${actualCost.toDouble()}")

    // Estimate the Planned Value(PV) and the Earned Value(EV) calculations
    var plannedValue = plannedPercentComplete.toDouble() * budgetAtCompletion.toDouble()
    var earnedValue = actualPercentComplete.toDouble() * budgetAtCompletion.toDouble()


    println("The estimated planned value is: $$plannedValue")
    println("The estimated earned value is: $$earnedValue")

    // Call the cost variance function
    var result = costVariance(earnedValue, actualCost.toDouble())
    // Check if the result is either a positive or negative variance; if negative the project is over budget
      if(result > 0) {
        println("The project is under budget!")

    } else {
        println("The project is over budget!")
    }
    println("The cost variance is: $${result.toDouble()}")

    // Estimate the cost performance index(CPI)
    var CPI = earnedValue.toDouble() / actualCost.toDouble()
    println("The cost performance index is: ${CPI}")
    // Check if the value of the CPI is greater than 1; if less than 1 the project is over budget
    if (CPI >= 1.0) {
        println("The project is under budget")

    } else {
        println("The project is over budget")
    }

    //Call the schedule variance(SV)function
    var resultSV = scheduleVariance(earnedValue.toDouble(), plannedValue.toDouble())
    // Check if the result is either a positive or negative variance; if negative project is behind schedule
     if (resultSV > 0) {
         println("The project is ahead of schedule!")
     } else {
         println("The project is behind schedule!")
     }
     println("The schedule variance is: $${resultSV.toDouble()}")

     // Estimate the schedule variance index(SPI)
      var SPI = earnedValue.toDouble() / plannedValue.toDouble()
      println("The schedule performance index is: $SPI")
    // Check if the SPI is greater than 1; if less than 1 the project is behind schedule
      if (SPI >= 1.0) {
          println("The project is ahead of schedule")
      } else {
          println("The project is behind schedule")
      }

    // Calculate the Estimate at completion(EAC) and use exception handling to check for division by zero
      var EAC = budgetAtCompletion.toDouble() / CPI.toDouble()

      if (CPI == 0.0) {
        try // throw an exception
        {
            var EAC = budgetAtCompletion.toDouble() / 0.0
            println("An error has occured.")
        }
        catch (e: ArithmeticException) { // catch and handle the exception
            println("Division by zero not allowed!")
        }
    }
     println("$$EAC is the estimate at completion")
     // Calculate the Estimate to Complete(ETC)
    var ETC = EAC.toDouble() - actualCost.toDouble()
    println("$$ETC is the Estimate to Completion")

     // Calculate the Variance of completion(VAC)
    var VAC = budgetAtCompletion.toDouble() - EAC.toDouble()
    println("$$VAC is the Variance at Completion")

      // To-Complete performance Index(TCPI)
     var TCPI = (budgetAtCompletion.toDouble() - earnedValue.toDouble()) /
            (budgetAtCompletion.toDouble() - actualCost.toDouble())


}


    // Use function declarations below to estimate the cost and schedule variances
fun costVariance(earnedValue: Double, actualCost: Double): Double
{
    return earnedValue - actualCost
}


fun scheduleVariance(earnedValue: Double, plannedValue: Double): Double {
    return earnedValue - plannedValue
}
