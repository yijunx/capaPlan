# capaPlan
ultimate capacity planning tool<br />
Here is the what we want to achieve<br />
bucket is a tool, not a job
The essence is to move from doing the tasks to doing the tasks that do the tasks.<br />

Understand that our job is full of repetitions. <br />
Because of repetition (and inefficiency of shared files, humongous excel files, antique software), <br />
Time is not spent in the most value adding way. There is too much time spent in creating/validating/scrutinizing a capacity file than analysing it and make the most value out of it.
A method to represent/recreate/reanimate the way how capacity file is generated (cleanly/openly/sustainably) is urgently needed.

why urgent
the number of scenario are increasing, so is the complexity, thus much more time is spent in trouble shooting<br />
    half a day to dead line yet we are not sure how cycle time altered some numbers<br />
the number of people are reducing <br />
    we need a more efficient method<br />
the jobs people do contain a big portion of repetition <br />
    this will reduce amoutn of repetition and divert the energy to more value adding tasks<br />
we also need a 1 stop sauce file as the base number we used in capacity planning, not that people no need to ask around <br />
    hi, what is the rpt of xxxxxxxx<br />
or check the some official file which is outdated, or not practical <br />

cleanly:<br />
    one number one file one name of its kind, ONLY<br />
    all the files should have version control<br />
    all the files should have standardized format, if not, warning follows<br />
    grow the inclination to work towards least amount of exception possible<br />
    reduce the eyeball tasks when we do adder (eg... small ls)<br />
    will not do adder halfway, disturbed, forget to finish<br />

openly:<br />
    currently the capacity calculation program is a black box to IE<br />
    the capacity planners are not in control of the capacity planning tool<br />
    thus we need a new program to have the openness, flexibility yet required a high degree of standardization<br />
        (PDM is too closed and excel is too flexible)<br />
        
sustainability:
    the success of a project does not mean work well once, but work well all the time and require least amount of maintenance<br />
    why python offers a high degree of sustainability:<br />
        it language is readable<br />
        OOP will make sure each method is short and clean<br />
        unlike excel, we are lost in tracing the formulas<br />
        here in python, it is readable<br />
        VBA is just impossible to maintain and too slow<br />
        why the past project failed<br />
    


What will be achieved:<br />
hopefully, with this we are able to cater for all kinds of requests in a more pleasant way, and the same job will not require more effort than a few lines of code.<br />
the rest of time, we could <br />
    dedicate to make this system more and more robust <br />
    spend more time to be as real IE <br />
    
what help is needed:<br />
volunteered team<br />
volunteered time in this time of lacking headcount in the team<br />
we understand that ..<br />

here is why python is chosen:<br />

it is an robust and up-to-date language<br />
code somehow follows english grammar<br />
it is an OOP language<br />
fast to learn<br />

why company software + excel is abandoned:<br />

company software is developed in the 1999, function is rigid, thus we invented ADDER to make it flexible<br />
ADDER in excel made thins better, also made things worse (chaotic version control, un-savable shared files, unreadable excel super long formulas, super inefficient VBA codes)<br />

        
        
    

thus we need to: <br />
    1. Create a capacity simulation tool that is suitable for most of the manufacturing environments.<br />
    2. Create a scenario study pack to analyse what if conditions, and give summaries<br />
    3. move on to the capex changes<br />
