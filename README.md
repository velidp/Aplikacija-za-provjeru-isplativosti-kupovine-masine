# Cost effectiveness check
## System for deciding on the cost-effectiveness of purchasing a new machine

The application is used to check the cost-effectiveness of buying a new machine. The user enters parameters that describe the machine and information on the costs of workers working with that machine. Based on the entered parameters, the application calculates and displays additional information about the machine and displays text about whether the machine is profitable or not. The graphical user interface is intuitive and easy to use. 

## Getting Started

To access the code and test the project, clone the repository and run it in Visual Studio.

## Application description
The data entered are divided into four categories.

In the **_Performance records_** category, the user enters the following parameters:  
_-Number of correctly produced pieces_  
_-Number of incorrectly produced pieces_    
_-The price of one piece_  

The following parameters are entered in the **_Machine costs_** category:  
_-Purchase value of the machine_   
_-Number of months of repayment_  
_-Depreciated value_  
_-Monthly costs of machine maintenance and servicing_  
_-Monthly costs of tools, accessories and equipment_  

In the **_Worker costs_** category, the following parameters must be entered:  
_-Number of working hours per month_  
_-The price of one working hour_  
_-Bonuses_  

The following two parameters are entered in the **_Income_**:  
_-Subsidies and incentives_  
_-By-byproducts_  

The initial appearance of the graphical user interface is shown in the following figure:
<p align="left">
  <img src="https://raw.githubusercontent.com/velidp/System-for-deciding-on-the-cost-effectiveness-of-purchasing-a-new-machine/master/GUI/GUI%201.png" width="800">
</p>  

After the user enters the parameters listed above, clicking the **_OK_** button in the **_Results_** box displays the calculated values. The values that the application calculates based on the entered parameters are:  
_-Profit from production_  
_-Production losses_  
_-Total number of pieces_  
_-Worker costs_  
_-Machine costs_  
_-Total cost_  
_-Total revenue_  
_-Profit_  

Based on the calculated application parameters in the **_Conclusion_** box, after the application user clicks the **_Show conclusion_** button, the text _"The machine is cost-effective"_ or _"The machine is not cost-effective"_ is displayed.

If the condition _if (profit * repayment period) <= (purchase value of the machine)_ is met, the application displays the text _"The machine is not cost-effective"_. An example of the data for which this condition is met and the final appearance of the graphical user interface for such data is shown in the following figure:

<p align="left">
  <img src="https://raw.githubusercontent.com/velidp/System-for-deciding-on-the-cost-effectiveness-of-purchasing-a-new-machine/master/GUI/GUI%202.png" width="800">
</p>  

If the previous condition is not met, ie. if the condition if (profit * repayment period)> (purchase value of the machine) is fulfilled, the application prints the conclusion _"The machine is cost-effective"_. The layout of the graphical user interface for this case is shown in the following figure:

<p align="left">
  <img src="https://raw.githubusercontent.com/velidp/System-for-deciding-on-the-cost-effectiveness-of-purchasing-a-new-machine/master/GUI/GUI%203.png" width="800">
</p>  

## Prerequisites

To run and use the application, download the file "System for deciding on the cost-effectiveness of purchasing a new machine" from the __*Executable File*__ folder.


## Built With

* [Python](https://www.python.org) - Programming language used
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - Standard GUI (Graphical User Interface) package


## Acknowledgments

* This is open source project.
* The application was developed with the intention of practicing Python programming and the use of Tkinter modules through its development.
