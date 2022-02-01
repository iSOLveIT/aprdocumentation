##############################
Discover model
##############################

Apromore allows us to discover a process map or a BPMN model from an event log. A process map (a.k.a. directly-follows graph) is a visual representation of the log as a graph where nodes capture process activities and directed arcs between them capture sequential order relations between the activities. For example, an arc going from activity *Accept order* to activity *Check order* indicates that in the log, we can observe that process cases flow from *Accept order* to *Check order*. Process maps are a simple yet effective means to understand the basic order of relationships between process activities. As such, they are the most common type of model discovered by commercial process mining tools.

-------------------
 View process map
-------------------

To view the process map, double-click on a log. Alternatively, we can select a log from the repository and click on *Discover > Discover model*.

|image1|

A window will open up, showing the process map discovered from the log.

|image2|

--------------------
Abstraction Settings
--------------------

We can adjust the complexity of the discovered map by increasing or decreasing the frequency or duration of nodes and arcs visualized in our process map. The default values for the nodes and arcs sliders are 100% and 10%, respectively.

We can abstract a process map by *Case frequency* or *Average Duration*. For example, if we abstract by case frequency and shift the arcs or nodes slider towards the left, more edges/nodes with low case frequency will be removed from the process map.

|image3|

Similarly, if we abstract by *Average Duration* and shift the arcs or nodes slider towards the left, more edges/nodes with low average duration will be removed from the process map.

|image4|

----------------------
Log statistics
----------------------

We can also check more detailed statistics. To inspect individual cases, use the *Case Inspector*. To open the *Case Inspector*, click on the number of cases under the *Log statics* section.

|image4.1|

The *Case Inspector* window will open.

|image4.2|

 Click on a specific case to visualize it exclusively in the Process Discoverer.

|image4.3|

To check the length of the cases, click on the *Activity instances* column. Cases will be sorted from the shortest to the longest.

|image4.4|

We can also sort them by pathway, using the *Case variant ID* column or by the Frequency of the pathway - *Percentage(%)* column.

|image4.5|

To download the list of cases and their statistics, click on *Download*.

|image4.6|

 To inspect individual activity, use the *Activity Inspector*. To open the *Activity Inspector*, click on the number of activities under the Activities chart in *Log statics* section.

|image4.7|

The *Activity Inspector* window will open.

|image4.8|

 To check the length of the activity, click on the *Activity instances* column. To check activity variant frequency, click on *Percentage(%)* column.

|image4.9|

To download the list of activities and their statistics, click on *Download*.

|image4.10|

To check the individual activity statistics, we can simply click on the activity.
We can also select multiple activities at once by pressing *Ctrl and dragging the mouse over* the part of the model which consists of these activities.

|image4.11|

----------------------
Visualize by Frequency
----------------------

We can also view the event log's simple statistics, such as the total, median, minimum, maximum, and average number of times an activity is executed. This information is provided as a label on the activities/arcs, color of activities, and arcs' thickness. The darker the blue color, the higher the number of times that activity has been observed in the log. The thicker arc, the higher the frequency of that arc. We can use the Frequency drop-down list in the *Visualization settings* section to view different statistics.

|image5|

----------------------
Visualize by Duration
----------------------

Additionally, we can view the statistics on the time performance of the activities and arcs in the process map using the *Duration drop-down list* in the *Visualization settings* section. These are total, mean, median, minimum, maximum, and average duration of each arc (indicating the waiting time before starting a given activity, once the previous one has been completed), and total, mean, median, minimum, maximum, and average duration of each arc duration of an activity (a.k.a. the activity’s processing time). Suppose the log only has completion timestamps for each activity and not their start timestamp. In that case, these performance statistics will combine both processing time and waiting time into a single time statistics visualized on the arc. At the same time, activities will be shown as having an instantaneous duration.

Like frequency statistics, we can also visualize time performance statistics via labels on activities and arcs and via colors and line thickness (on a red scale) for activities and arcs.

|image6|

------------------------------------
Visualize by Frequency and Duration
------------------------------------

We can also view both *Frequency* and *Duration* at the same time by clicking the |image6.1|. For example, if we are viewing our process map in *Frequency* mode, we can also view the *Duration* as a secondary metric by clicking on the |image6.1|.

|image7|

------------------------------------
Visualize by Different Perspectives
------------------------------------

Visualizing the handover between activities is not the only way a process can be analyzed. There will be times when we may be interested in assessing if a specific resource or group of resources are overloaded with work. When clicking on *Perspective* we can decide which attribute of the log will focus on the process map.

|image8|

For example, to visualize the handover of work among a group of resources, we can select the *Resources* option. This option will map each actor's organizational role in our process to a node and connect two nodes if a handover of work occurs between the two nodes.

|image9|

-----------
Filter Log
-----------

When analyzing an event log, we may be interested in isolating a particular type of behavior or removing a specific activity. An event log can be filtered by clicking on the *Filter* icon and creating a new filter that fits our needs. For more information on the optimal use of *Filter*, we suggest viewing the `Filter Log manual <https://apromore.org/help/user-manual/discovery/filter-log/>`_.

|image10|

----------------
View BPMN Model
----------------

Whenever the insights deriving from the analysis of a process map are not sufficient, the same functionalities are offered on top of a BPMN model. Changing the view from *Process Map* to *BPMN model* will automatically discover a BPMN model from an event log. When visualizing a BPMN model, the slider *Parallelism* offers the possibility to adjust the amount of parallelism (e.g., AND and OR gateways) discovered by the plugin.

|image11|

------------------------------
Export Process Map/BPMN Model
------------------------------

A filtered log or discovered process map/BPMN can be exported by clicking on the different save buttons to export the model as a “.bpmn”, a PDF, PNG, or a JSON file.

|image12|

------------------------------
Animate Log (Process Map)
------------------------------

The *Animate* button allows us to replay the log on top of the process map, using the *Animate a log* on top of the process map feature.

|image13|

.. _searchPD:

-----------------
Search Activity
-----------------

We can also search for an activity by using the search bar on the top-right.

|image14|

For ease of view, the search results get highlighted in the process map.

|image15|


.. |image1| image:: /images/discovermodel/1.png
.. |image2| image:: /images/discovermodel/2.png
.. |image3| image:: /images/discovermodel/3.png
.. |image4| image:: /images/discovermodel/4.png
.. |image4.1| image:: /images/discovermodel/4.1.png
.. |image4.2| image:: /images/discovermodel/4.2.png
.. |image4.3| image:: /images/discovermodel/4.3.png
.. |image4.4| image:: /images/discovermodel/4.4.png
.. |image4.5| image:: /images/discovermodel/4.5.png
.. |image4.6| image:: /images/discovermodel/4.6.png
.. |image4.7| image:: /images/discovermodel/4.7.png
.. |image4.8| image:: /images/discovermodel/4.8.png
.. |image4.9| image:: /images/discovermodel/4.9.png
.. |image4.10| image:: /images/discovermodel/4.10.png
.. |image4.11| image:: /images/discovermodel/4.11.png
.. |image5| image:: /images/discovermodel/5.png
.. |image6| image:: /images/discovermodel/6.png
.. |image6.1| image:: /images/discovermodel/6.1.png
    :width: 30
.. |image7| image:: /images/discovermodel/7.png
.. |image8| image:: /images/discovermodel/8.png
.. |image9| image:: /images/discovermodel/9.png
.. |image10| image:: /images/discovermodel/10.png
.. |image11| image:: /images/discovermodel/11.png
.. |image12| image:: /images/discovermodel/12.png
.. |image13| image:: /images/discovermodel/13.png
.. |image14| image:: /images/discovermodel/14.png
.. |image15| image:: /images/discovermodel/15.png
