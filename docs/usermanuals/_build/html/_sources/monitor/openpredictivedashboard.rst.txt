##############################
Open predictive dashboard
##############################

.. note:: Apromore’s predictive monitoring plugins are available as add-ons to Apromore Enterprise Edition.

Once the predictive models have been trained, they can be deployed to the Runtime predictive monitoring environment of Apromore, to make predictions on ongoing cases. The Runtime plugin bundle can be used to stream an event log from the repository, or hook into an external stream. Either way, the input stream is transformed into a stream of predictions which is visualized in a Web-based dashboard.

To use the plugin, select an event log from the repository and click on *Monitor -> Predictively monitor log*. For demonstration purposes, Apromore repository provides several pre-processed logs under Examples/Predictive Monitoring folder. These logs can also be downloaded from `here <https://drive.google.com/file/d/1ZATjpBMSjgxLDKdIvLOJ15NRz_N0b6K0/view>`_


|image1|

Create a new Predictive Monitor.

|image2|

Select the created monitor and click *Stream log to dataflow*.

|image3|

Click *Show dashboard* to start streaming events from the log. A dashboard will show up and populate with ongoing cases:

|image4|


The dashboard provides a list of currently ongoing as well as completed cases. For each case, it is also possible to visualize a range of summary statistics including the number of events in the case, its starting time and the time when the latest event in the case has occurred. For the ongoing cases, the Runtime plugin bundle provides the predicted values of the performance indicators the user wants to predict. For completed cases, instead, it shows the actual values of the indicators. Color-coding is applied to help users quickly nail down potentially problematic cases.

-----------------------------------------
Export performance predictions into CSV
-----------------------------------------

In addition to the dashboard for continuous real-time process monitoring, the Runtime plugin supports a *regular reports* use case where users can get reports in a CSV format on a regular basis with the current set of predictions. These reports can be readily imported into common data analytics platforms (e.g. Microsoft Excel, Tableau, QlikView, R) for further exploration and visualization.

|image5|

A screencast of this plugin can be found `here  <https://www.youtube.com/watch?v=Q4WVebqJzUI&feature=youtu.be>`_ .


.. |image1| image:: /images/openpredictivedashboard/1.png
.. |image2| image:: /images/openpredictivedashboard/2.png
.. |image3| image:: /images/openpredictivedashboard/3.png
.. |image4| image:: /images/openpredictivedashboard/4.png
.. |image5| image:: /images/openpredictivedashboard/5.png
