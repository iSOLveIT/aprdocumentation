##############################
Create data pipeline
##############################

The Create data pipeline plugin, also referred as the ETL plugin, allows users to compose event logs from one or more tables or data sources.
It aims to integrate data from multiple sources by extracting, transforming, and loading to gain essential business insights for competitive advantage.
To define a data pipeline, click on *Create data pipeline* button.

|image1|

.. note:: We can also select the *Create data pipeline*  option from the *File* menu drop-down.

|image1.1|

The Extract-Transform-Load view appears after clicking on create data pipeline.

.. note:: We can switch between three main views. However, to create the insightful result, it is essential to complete steps in the default order: Extract - Transform - Load.

|image2|

-----------------------
Extract data
-----------------------

We can extract data through two options – *Local File System* and *DB Connections*.
The corresponding buttons are placed in the left pane right under the *Extract view*.

.. note:: We can extract tables from relational databases and upload files in CSV and Parquet formats from the local system.

|image3|

To upload a file from the personal computer, click on the icon in the right corner of the *Local File System*.

|image4|

To begin uploading a file from the database, click on the “+” icon in the right corner of the *DB Connections*.

|image4.1|

When *Add New Database Connection* window appears, insert all the details, choose the suitable options from the *Database Type* and *Connection Type* drop-downs and click on *Connect*.

|image4.2|

To delete a file, click on the *Trash bin* - |image4.2.1| right next to it.

|image4.3|

When at least 2 logs are uploaded, merge them by selecting the relevant join type from the *Join Type* drop-down menu and appropriate keys.


  .. figure:: /images/createdatapipeline/5.png
     :alt: image5
     :class: with-shadow

     INNER JOIN - Returns records that have matching values in both tables;
     FULL JOIN - Returns all records when there is a match in either left or right table;
     LEFT JOIN - Returns all records from the left table, and the matched records from the right table;
     RIGHT JOIN - Returns all records from the right table, and the matched records from the left table;


After all the files are uploaded, table keys and the join type are chosen, click on *Submit*.

|image5.1|

The table obtained by joining the two logs appears right beneath the *table and join selections*.

|image6|

-----------------------
Transform data
-----------------------

There are 2 main areas in the Transform view - the list of tables containing all the columns from the extracted logs (marked blue) and the transformed table (marked red).

.. note:: To complete transformation, we must select at least three compulsory columns: case id, activity, and timestamp

|image7|

To add the column from the list to the transformed table, click on the "+" button next to the column name.

|image8|

.. note:: In the case of large logs, the addition of columns might take some time. Do not click on the same column several times to prevent column duplicates in the transformed table.

To add the whole extracted table to the *Transformed table*, click the "+” button next to the table name. The tables are marked as |image9|

|image10|

To rename the column, click on |image10.1| right next to the column name.

.. warning:: Spaces in the column name aren't supported.

|image11|

To delete the column from the Transformation table, click on the red "X" button next to *Rename*.

|image12|

.. note:: If the column was deleted by mistake or becomes necessary, we can easily add it to the table again from the columns list.

|image13|

To add a customized column that is not present in any of the tables, click on *+ New column* button placed in the upper right corner beneath *Manage data pipelines button*.

|image14|

After a new column window appears, enter the new column name and click *Create*.

|image15|

To check or change the values of the column, click *Edit rules* right beneath the name of the necessary column.

|image16|

Edit rules window appears. The default rule is displayed. In addition to different join operations, we can create columns in the event log by composing existing columns using arithmetic, concatenation, and find-and-replace operations. For example, you can add a *Cost* column to an event log and compute this cost based on the hourly rate of your resources and the duration of tasks.

|image17|

We can add a new rule by clicking *+ Add new rule*.

|image18|

To apply the rule, after the condition is set, click on *OK*.

|image19|

-----------------------
Load data
-----------------------

When we click on Load view, the transformed log is displayed.

|image20|

Click on *Detect* to automatically detect encoding option.

|image21|

We can opt not to import a column by attaching the *Ignore tag* to it. To make it easier to ignore multiple columns, we can click on the *Event attribute* -> *Ignore button* at the upper-left corner. From that point on, any column we select becomes tagged with *Ignore*.

|image22|

Similarly, if we need to tag multiple columns as *Event attribute*, we can click on *Ignore* –> *Event Attribute* in the upper-left corner next to *Event attribute* -> *Ignore*. From that point on, any column we select becomes tagged with *Event Attribute*.

|image23|

Click on *Upload Log* to finish the import.

|image24|

The *Save Log As* dialog box appears. Enter the log name and choose the destination folder from the drop-down. Click on *Upload* to successfully import the log into Apromore.

|image25|



.. |image1| image:: /images/createdatapipeline/1.png
.. |image1.1| image:: /images/createdatapipeline/1.1.png
.. |image2| image:: /images/createdatapipeline/2.png
.. |image3| image:: /images/createdatapipeline/3.png
.. |image4| image:: /images/createdatapipeline/4.png
.. |image4.1| image:: /images/createdatapipeline/4.1.png
.. |image4.2| image:: /images/createdatapipeline/4.2.png
.. |image4.2.1| image:: /images/createdatapipeline/4.2.1.png
    :width: 20
.. |image4.3| image:: /images/createdatapipeline/4.3.png
.. |image5| image:: /images/createdatapipeline/5.png
.. |image5.1| image:: /images/createdatapipeline/5.1.png
.. |image6| image:: /images/createdatapipeline/6.png
.. |image7| image:: /images/createdatapipeline/7.png
.. |image8| image:: /images/createdatapipeline/8.png
.. |image9| image:: /images/createdatapipeline/9.png
	  :width: 20
.. |image10| image:: /images/createdatapipeline/10.png
.. |image10.1| image:: /images/createdatapipeline/10.1.png
	  :width: 20
.. |image11| image:: /images/createdatapipeline/11.png
.. |image12| image:: /images/createdatapipeline/12.png
.. |image13| image:: /images/createdatapipeline/13.png
.. |image14| image:: /images/createdatapipeline/14.png
.. |image15| image:: /images/createdatapipeline/15.png
.. |image16| image:: /images/createdatapipeline/16.png
.. |image17| image:: /images/createdatapipeline/17.png
.. |image18| image:: /images/createdatapipeline/18.png
.. |image19| image:: /images/createdatapipeline/19.png
.. |image20| image:: /images/createdatapipeline/20.png
.. |image21| image:: /images/createdatapipeline/21.png
.. |image22| image:: /images/createdatapipeline/22.png
.. |image23| image:: /images/createdatapipeline/23.png
.. |image24| image:: /images/createdatapipeline/24.png
.. |image25| image:: /images/createdatapipeline/25.png
