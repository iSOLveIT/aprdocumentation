##############################
Simulate process
##############################

Apromore allows users to simulate .bpmn models to understand how the business process will look and work in different scenarios.

We can do the simulation of process models in Apromore by performing two steps:

- Specification of simulation parameters
- Creation of simulated log

Double-click the BPMN model to open it.

|image1|

A window will open up, showing the selected BPMN model.

|image2|

---------------------------------------------------
Specification of simulation parameters
---------------------------------------------------

To specify simulation parameters, click on the *Toggle simulation parameters panel* button.

|image3|

The simulation panel with different parameters to be specified will appear from the BPMN editor window's right side

|image4|

.. note:: If we want to hide the parameters panel, we can always click on the ">>" sign located at the right side of the panel and click on it once again to make it visible.

|image34|

The parameters are organized into different tabs. For convenience, it is recommended to fill it in the following order: *General -> Timetables -> Resources -> Tasks -> Gateways*.

.. note:: We can`t proceed without the specification of the mandatory parameters. These are marked red.

|image5|

---------------------------
General parameters tab
---------------------------

The inter-arrival time is the time between each arrival of the process instances. It shows how frequently a new process instance starts.

Apromore offers a variety of options for inter-arrival time, as shown below.

|image6|

The value denotes the inter-arrival time unit. In the following example, the inter-arrival time is fixed and equals 5 hours, meaning that a new process instance starts every 5 hours.

|image7|

The total number of process instances shows how many BPMN process instances start in the simulation scenario.

|image8|

.. note:: For preventing us from entering incorrect values, Apromore displays inline alert messages signaling that we need to recheck the data.

|image10|

We can specify the simulated scenario start date and time to determine when the first process starts.

|image11|

We can exclude a certain percentage of statistics from the start and the end of the process instances that fall between the start and the end time of the simulation scenario. This is usually done, considering the availability of resources and activities that are handled without any delays.

|image12|

For the cost calculations, we may choose a suitable currency from the drop-down list.

|image13|

-----------------------------------------------------
 Timetables, Resources and Tasks parameters tabs
-----------------------------------------------------

After we finished entering the general tab information, we then switch to the *Timetables* tab.

|image20|

While adding the new timetable, it is required to name it and specify the working timeslot

|image21|

.. note:: One timetable may consist of many different timeslots. This is very useful when workers (also known as actors/resources) work in shifts.

In the example below, workers who follow "Timeslot 3" from "Timetable-1" work five days (Monday-Friday) from 8.00 till 17.00.

|image22|

In the "Resources" tab,  the default resource is created automatically.

|image17|

To add the new resource, select it from the list and press "+". To delete it, select and then press "x".

|image18|

Specify all the resource details required in the new resource window, which loads right after clicking on "+".

|image19|

Number of Resources is the amount of the new resource type actors participating in this scenario. Cost per hour is the amount the resource earns per hour working.

A timetable is assigned to a resource from the *Resource timetable* drop-down list.

|image23|

After we finished entering the information in the *Resources* tab, we then switch to the *Tasks* tab.

|image14|

Click on a task in the BPMN model in order to set the simulation parameters for the task. The simulation parameters of a task are:

• The resource pool responsible for performing this task

• The probability distribution of the task duration and the parameters of this distribution (e.g. the mean in the case of an exponential distribution).The duration of the task is the time it takes for a resource to execute one instance of a task. Please note that the duration of a task must not include the waiting time before the start of the task. It should only include the processing time.

|image15|

.. note:: For a model to be simulated, the tasks must be untyped (Abstract). Apromore does not currently support the simulation of process models where some of the tasks have a type such as *User task*, *Service task*, etc.

We can use an alternative approach for more complex models by just clicking on the task we would like to change. The task details window will open automatically.

|image29|

----------
Gateways
----------
Gateways is a BPMN notation used to control how a process flows.
Gateways can be exclusive (XOR), meaning that precisely one alternative path can be selected or inclusive (OR), meaning that there can be several paths.

|image25|

All gateway elements in the BPMN model require execution probabilities for their outgoing sequence flows.

|image26|

.. note:: The sum of the probabilities for the execution of each gateway must be 100%.

|image27|

After we entered the simulation parameters, we can save the model.

|image28|

When the save dialog appears, click *OK*.

|image30|

To simulate the saved model, go to the main workspace -> *Analyze -> Simulate model*.

|image32|

To save the simulated log, click on *Save*.

|image35|

The simulated log appears in the workspace.

|image37|

.. note:: Suppose, for some reason (for instance, the model was quite complex with the variety of tasks and many resources), we ignored the mandatory data lines and didn`t specify them before. In that case, Apromore will display the list of errors to correct them.

|image33|

We can view a range of statistics for simulated logs, including case duration, case duration within timetable, case waiting time, cycle time, waiting time, and cost in dashboards.

|image38|

In addition to this, we can simulate two what-if scenarios.
We can then compare the simulated logs by animating 2 logs against the BPMN model by going to the main workspace, selecting 2 logs and BPMN model -> *Analyze -> Simulate model*.

|image39|

A window will open up, showing the simulation overview.

|image40|


.. |image1| image:: /images/processmodelsimulation/1.png
.. |image2| image:: /images/processmodelsimulation/2.png
.. |image3| image:: /images/processmodelsimulation/3.png
.. |image4| image:: /images/processmodelsimulation/4.png
.. |image5| image:: /images/processmodelsimulation/5.png
.. |image6| image:: /images/processmodelsimulation/6.png
.. |image7| image:: /images/processmodelsimulation/7.png
.. |image8| image:: /images/processmodelsimulation/8.png
.. |image10| image:: /images/processmodelsimulation/10.png
.. |image11| image:: /images/processmodelsimulation/11.png
.. |image12| image:: /images/processmodelsimulation/12.png
.. |image13| image:: /images/processmodelsimulation/13.png
.. |image14| image:: /images/processmodelsimulation/14.png
.. |image15| image:: /images/processmodelsimulation/15.png
.. |image16| image:: /images/processmodelsimulation/16.png
.. |image17| image:: /images/processmodelsimulation/17.png
.. |image18| image:: /images/processmodelsimulation/18.png
.. |image19| image:: /images/processmodelsimulation/19.png
.. |image20| image:: /images/processmodelsimulation/20.png
.. |image21| image:: /images/processmodelsimulation/21.png
.. |image22| image:: /images/processmodelsimulation/22.png
.. |image23| image:: /images/processmodelsimulation/23.png
.. |image24| image:: /images/processmodelsimulation/24.png
.. |image25| image:: /images/processmodelsimulation/25.png
.. |image26| image:: /images/processmodelsimulation/26.png
.. |image27| image:: /images/processmodelsimulation/27.png
.. |image28| image:: /images/processmodelsimulation/28.png
.. |image29| image:: /images/processmodelsimulation/29.png
.. |image30| image:: /images/processmodelsimulation/30.png
.. |image32| image:: /images/processmodelsimulation/32.png
.. |image33| image:: /images/processmodelsimulation/33.png
.. |image34| image:: /images/processmodelsimulation/34.png
.. |image35| image:: /images/processmodelsimulation/35.png
.. |image37| image:: /images/processmodelsimulation/37.png
.. |image38| image:: /images/processmodelsimulation/38.png
.. |image39| image:: /images/processmodelsimulation/39.png
.. |image40| image:: /images/processmodelsimulation/40.png
