##################################
Schedule/Manage Data Pipeline
##################################

:doc:`Create data pipeline <createdatapipeline>` allows to update logs automatically by scheduling. After scheduling a pipeline, the logs will be fetched directly from the database and transformed according to the set transformation.

We can also manage the scheduled pipelines.

--------------------
Schedule pipeline
--------------------

To schedule pipeline, go to the *Load* view and click on the *Schedule pipeline* button placed in the right corner under the *Manage Data Pipelines* button.

|image1|

The *Schedule Data pipeline* window appears.

|image2|

We can choose the frequency of the updates – hourly, daily, weekly, or monthly to extract, transform, and load event logs into Apromore.

|image3|

To run pipeline instantly, tick the box *Run pipeline now in addition to the scheduled time* placed right beneath the frequency settings.

|image4|

When frequency settings are complete, choose the *Log name* and *Log destination* and click on *Schedule*.

|image5|

-------------------
Manage pipeline
-------------------

To check or edit scheduled pipelines, click on *Manage Data Pipelines* button placed in the right corner under the user's details.

|image6|

The *Data pipeline Management* window appears, displaying all the scheduling-related details next to the pipeline name: time/frequency of loads, status, last run.

|image7|

.. note:: By default, the window shows all the pipelines. To see only Running or Paused ones, click on the corresponding section.

|image7.1|

We can pause or unpause the pipeline by moving the *pipeline activation slider* next to the pipeline name.

|image8|

To view the details of all the updates of the scheduled pipeline, click on |image8.1|

.. note:: The status of the pipeline run might be either success or fail, where fail means that for some reason system wouldn't able to run the scheduled pipeline successfully.

|image9|

To delete the scheduled pipeline, click on |image9.1|

|image10|

To run pipeline now, click on |image10.1|

|image11|

To close the *Data Pipeline Management* window, click on the "X" button in the upper right corner of the window.

|image12|

To refresh the window, click on |image12.1|

|image13|



.. |image1| image:: /images/managepipeline/1.png
.. |image2| image:: /images/managepipeline/2.png
.. |image3| image:: /images/managepipeline/3.png
.. |image4| image:: /images/managepipeline/4.png
.. |image5| image:: /images/managepipeline/5.png
.. |image6| image:: /images/managepipeline/6.png
.. |image7| image:: /images/managepipeline/7.png
.. |image7.1| image:: /images/managepipeline/7.1.png
.. |image8| image:: /images/managepipeline/8.png
.. |image8.1| image:: /images/managepipeline/8.1.png
	  :width: 20
.. |image9| image:: /images/managepipeline/9.png
.. |image9.1| image:: /images/managepipeline/9.1.png
	  :width: 20
.. |image10| image:: /images/managepipeline/10.png
.. |image10.1| image:: /images/managepipeline/10.1.png
	  :width: 20
.. |image11| image:: /images/managepipeline/11.png
.. |image12| image:: /images/managepipeline/12.png
.. |image12.1| image:: /images/managepipeline/12.1.png
	  :width: 20
.. |image13| image:: /images/managepipeline/13.png
.. |image14| image:: /images/createdatapipeline/14.png
