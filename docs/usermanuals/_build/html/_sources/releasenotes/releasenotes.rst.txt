##########################
Version 8.0
##########################

*Release Date: November, 2021*

----------------------
Feature/Enhancement
----------------------

**Custom Calendars**

* Apromore now provides the ability to create and edit custom calendars and to associate a custom calendar with an event log. When creating a calendar, you can include public holidays based on your location and add custom holidays to the calendar.

**Delta Analysis between process models**

* Apromore now allows you to compare two BPMN process models to perform delta analysis. For example, you can use delta analysis to compare a process model discovered from an event log (capturing the as-is process) with a reference process model (capturing a to-be process). When you compare two process models using delta analysis, the tool displays the differences and allows you to overlay the differences on top of the process models.

**Filter and Dashboard Templates**

* Apromore now provides the ability to save a filter or a dashboard template that you have defined on an event log, and to apply the saved template to another log. For example, you can create a dashboard template on an event log containing all the cases of an order-to-cash process that completed in October, and then copy it to an event log containing all the cases of the same order-to-cash process for the month of November.

**Internationalization**

* Apromore now provides the option to switch between different languages. Currently, we support English and Japanese, with German coming soon. New languages can easily be added.

**Support for Group Authorization**

* Apromore now supports group-based authorization using groups extracted from an external identity provider (SAML or LDAP).

**Anonymization**

* You can now choose to anonymize one or more columns during log import by selecting the “anonymization” icon on the columns you wish to anonymize. For example, you may anonymize sensitive information such as case IDs and resource names.

**Automatic data ingestion via the S3 connector**

* You can now ingest data into Apromore via our AWS S3 Connector. The logs can be pushed into S3 buckets via data ingestion pipelines, and picked up automatically by Apromore to be registered in Apromore’s repository. The S3 bucket can be hosted by Apromore or the customer, in their private AWS cloud. Encryption can be managed by AWS with customer-provided master key, or directly by the customer.

**Case and Event attribute on X and Y-axis**

* We have added more customization options to Apromore’s Dashboard. You can now display numerical or categorical case/event attributes on the X and Y-axis of any chart in a dashboard. For example, you can create a chart to display the number of resources (Y-axis) who perform each activity in the log (X-axis). If you select a numeric attribute in the Y-axis, you can also select an aggregation function such as average, total, median, etc. For example, you can create a chart that displays the countries on the X-axis and for each country, the total revenue on the Y-axis.

**KPI Thresholds and Reference lines**

* In the Dashboard, you can now set KPI thresholds and add reference lines for average and median, as well as custom reference lines, along both X and Y-axis. For example, you can choose to add a KPI threshold to separate the cases with a higher waiting time from those with a lower waiting time, or show the average number of active cases over time in the Work-in-Progress area chart.

**Exporting Dashboard Analytics to S3 buckets**

* Apromore now provides the capability to export dashboard analytics as CSV or Parquet files and save these locally or on an AWS S3 bucket.

**Between Filter**

* With a couple of clicks, you can now define a new filter criterion to retain or remove events between the first or last occurrence of a source and target node in the process map. For example, you can retain all events between the first occurrence of the “Send invoice” activity and the last occurrence of the “Receive payment” activity.

**Save and edit ETL data pipelines**

* Apromore now supports the ability to save and edit data ingestion pipelines. For example, you can now edit an existing pipeline by replacing the existing logs with an event log with the latest data.

**Performance Improvement in Dashboard**

* The performance of the operations performed on large logs in the dashboard has been improved.

**Case Variant Inspector**

* You can now inspect each case variant individually using the case variant inspector in the Process Discoverer plugin, and check out the value of attributes for each node in the variant.

-------------------------------
Improvements and Bug Fixes
-------------------------------
* **Improvement:** The start and end timestamps were exported in a single column when exporting an event log in CSV format. Now, both timestamps are placed in separate columns within the same row.

* **Improvement:** You can now choose to tag a column as a Perspective in the Log Importer. Once done, you can switch between these perspectives in Process Discoverer.

* **Improvement:** The Log Importer now supports ISO-8859-1 (Latin-1) encoding type.

* **Improvement:** An event log with a standard ISO-8601 format timestamp can now be imported into Apromore.

* **Improvement:** The ETL plugin now supports the ability to subtract two timestamps and trim a column value.

* **Improvement:** You can now upload zipped BPMN models

* **Improvement:** You can now set the name of the log when importing it into Apromore

* **Improvement:** A BPMN model shared with a viewer cannot be exported/modified.

* **Fix:** A log containing a case ID greater than 15 digits could not be uploaded.

* **Fix:** The labels on gateways in a BPMN model were not getting updated when changing them.

* **Fix:** Uploading files in Apromore using the ETL plugin used to throw an error when connecting to an S3 bucket with a name greater than 30 characters.

##########################
Version 7.20
##########################

*Release Date: June, 2021*

----------------------
Feature/Enhancement
----------------------

**Extract-Transform-Load (ETL) Console**

* Apromore now comes with a graphical ETL console that allows you to compose event logs from one or more tables or data sources. The ETL console allows you to define data pipelines to extract tables from relational databases, transform these tables to compose an event log, and load the resulting event log table into Apromore. In addition to different join operations, you can remove columns and create columns in the event log by composing existing columns using arithmetic, concatenation, and find-and-replace operations. For example, you can add a “Cost” column to an event log and compute this cost based on the hourly rate of your resources and the duration of tasks. You can also schedule a data pipeline to run hourly, daily, weekly, or monthly jobs to extract, transform, and load event logs into Apromore.

**Single Sign-on Support**

* Apromore can now be connected with your corporate identity system for single sign-on (SAML or OpenID).

**Storage in Amazon S3 buckets**

* Apromore now comes with an option to store your event logs in a dedicated Amazon S3 bucket for high reliability and security (available for enterprise licenses only). Your IT security team can be given rights to audit your tenancy’s S3 bucket. The data in your tenancy’s S3 bucket is protected at all times using either an Amazon S3-managed encryption key or an encryption key provided by your IT team. This enables your IT team to have full control over access to your event logs.

**Transfer Ownership**

* Before deleting a user, you can transfer ownership of all the assets (models, logs, analytics artifacts) to better manage business continuity.

**Fine-Grained Sharing**

* You can choose to share individual dashboards and filters associated with a log by giving a user restricted viewer rights. For example, when sharing an event log, you can choose which specific dashboards or filters you wish to share, as an alternative to sharing all the associated dashboards and filters.

**Case Length Filter**

* You can now filter out cases based on case length (number of activity instances in the case). For example, you can retain or remove all cases whose length is between 3 to 15 activity instances.

**Undo/Redo Filter**

* You can remove/reinstate a filter criterion using the undo/redo filter buttons in Process Discover.

**Performance Improvements in Filter**

* The performance of the filter operations on large logs has been improved.

**Look-and-feel improvements in Log Animator**

* The ability to hide/unhide tokens of a log in a multi-log animation has been introduced. You can also customize the color of the tokens.

**Report Issue**

* A Report Issue button has been introduced to allow users to report bugs.

**Recursive Folder Sharing**

* You can now share a folder in such a way that all sub-folders and files inside that folder are shared along, recursively.

-------------------------------
Improvements and Bug Fixes
-------------------------------
* **Improvement:** When trying to animate a syntactically incorrect process model, the log importer now shows user-friendly error messages.
* **Improvement:** You can now animate both process maps and BPMN models directly inside Process Discoverer.
*	**Improvement:** File names can now contain commas and periods
*	**Improvement:** A new “Generate report” function in the dashboard allows you to choose which tiles, charts, and tables you wish to include in the Word, PDF or Powerpoint report (or you can select “all” to include everything).
*	**Fix:** The BPMN editor gives an error message when you change the version number to a different format.
*	**Fix:** The shortcut for opening the arc duration filter is not working.
*	**Fix:** In the slice log window, the number of cases is incorrect.
*	**Fix:** Column names with accented letters are not displayed in the log importer.
*	**Fix:** When a logs contains empty column names, no data is shown in the log importer.
*	**Fix:** Access rights management window gives an error when the group name matches the user name.
* **Fix:** The fields in the user creation window are not validated
*	**Fix:** Incorrect error message is given when a file name contains more than 60 characters.

##########################
Version 7.19
##########################

*Release Date: January, 2021*

----------------------
Feature/Enhancement
----------------------

**Process Simulator**

* You can now attach a simulation scenario to a BPMN model and simulate a model with an attached simulation scenario. The output of a simulation is a simulated log. You can analyze a simulated log using all the functionality available in Apromore (Process Discoverer, Dashboard, etc.). In the Dashboard, you can view a range of statistics for simulated logs, including case duration, case duration within timetable, case waiting time, cycle time, waiting time, and cost.

**Node duration performance filter**

* You can filter out cases based on the node’s duration.

**Arc duration performance filter**

* You can filter out cases based on the arc’s duration.

**Secondary attribute filter**

* You can filter out cases based on two attributes simultaneously, for example, retain or remove all cases where there is an event with Activity = "Create order" (primary attribute) and Resource = "John Smith" (secondary attribute).

**Share filters and dashboards**

* Multiple users can edit filters and dashboards concurrently.

**Dashboard auto-saving**

* You can now choose whether or not to auto-save changes to your dashboards.

**Export dashboards**

* You can now export your dashboards in a variety of formats incl. Word and PowerPoint to create professionally looking reports.

**Timestamp format detection in CSV Importer**

* A wider range of timestamp formats are now supported.

**Timezone detection in CSV Importer**

* When you import a CSV/XLSX/Parquet file, the timezone is automatically detected.

**Import Parquet and XLSX files**

* You can upload a parquet or XLSX file.

**Performance and look-and-feel improvements in Log Animator**

* The responsiveness of the log animator has been improved. When a large number of tokens are stuck in the same arc, a bubble is shown instead of showing individual tokens.

##########################
Version 7.18
##########################

*Release Date: October, 2020*

----------------------
Feature/Enhancement
----------------------

**Portal grid view**

* You can browse through the folders and files in Apromore’s Portal in grid format (default mode) in addition to the old list format.

**Import log from URL**

* You can import a file from Dropbox, Google Drive, Microsoft OneDrive or from any URL.
* See: :ref:`Upload a file from URL <uploadafilefromurl>`

**Save and share filters**

* You can :ref:`save filters <savefilter>` associated with a log and share these filters alongside the event log.
* Note: Only the owner of an event log can save, edit, or remove the filters associated with that log. Other users can define temporary filters but not save them.

**Customize, save & share performance dashboards**

* You can add, remove, or customize any performance indicator, chart or table in the default views of the performance dashboard.
* You can add one or more custom views to the performance dashboard of a log. Custom views can be created from :ref:`existing views <createfromexisting>` or from :ref:`scratch <createfromscratch>`.
* You can save and share dashboards. All changes you make to a performance dashboard are saved together with the event log and are visible to all users who have access to the log.
* See: `Video demonstration of the new Performance Dashboard <https://www.youtube.com/watch?v=E_eJrgFLjRE&feature=youtu.be>`_.
* Note: Only the owner of a log can edit the performance dashboard of the log. Other users can make a copy of a log and customize the dashboard on a copy of the log

**Reusing CSV import schemas**

* When you import a CSV file, the mapping of the columns (schema mapping) is automatically saved. When you later import a CSV file with the same column headers, the CSV importer prompts a dialog box to let you choose whether to :ref:`apply the saved mapping <csvschemamapping>` or not.

**Clear applied filters**

* You can :ref:`clear all the filters <clearallfilters>` on the current log in Process Discoverer with a single click.

**Search box in Process Discoverer**

* A new :ref:`search box in Process Discover <searchPD>` allows you to search for a node (e.g. activity) by its name or a prefix of the name. All nodes that match the search string are highlighted.

**Enhanced users and groups management**

* You can grant access rights to any folder and file you own either to an individual user or to a group.
* Administrators can create groups and assign users to groups.
* See: :doc:`Users and groups management <../theapromoreportal/manageusersandgroups>`

**Download process performance stats from dashboard**

* You can download the data behind any chart or table in the performance dashboard in CSV format, or you can download all CSV files with the data in the performance dashboard in a single zip file

**Copying and moving logs or process models**

* You can copy or move files across the folders in the Portal via the :ref:`copy, cut, and paste icons <copycutpaste>`.

**Improved session management**

* We have made improvements to session management to improve performance and reduce session timeouts.

**LDAP Authentication**

* System administrators can more easily configure Apromore to connect to a corporate LDAP directory for authentication.


**New shortcuts for filtering**

* You can open the case filter, case variant filter, event filter, activity filter, performance and timeframe filters in one click from the Process Discoverer by clicking on the respective icons in the Log Statistics and Temporal statistics sections of the Process Discoverer.

**Relative case frequency overlay**

* You can now display the relative case frequency on each node/arc in the Process Discoverer. The relative case frequency is the percentage of cases in which a given node or directly-follows relation occurs.


----------------
Bug Fix
----------------

**Folder and file renaming**

* The portal gives an error message when you enter forbidden characters in file name.

**Handling of long labels**

* Fixed a bug that made long activity or node labels to go across the corresponding node in the process map/model.



##########################
Version 7.16
##########################

*Release Date: June, 2020*

* **New Features:**
    * Tiles of performance measures can now be created in custom dashboards. These can be useful to display a set of standard and user-defined KPIs, in addition to the custom charts
    * Aggregated log stats can now be exported from the Dashboard into CSV files
    * Reimplemented median calculations for frequencies and durations in Process Discoverer
    * Introduced “breadcrumbs” for easier Portal navigation
    * Process models and logs can now be searched for from the Search bar of the Portal

* **Improvements:**
    * Improved memory management across various plugins
    * Process models created by the Merge plugin are now automatically laid out
    * Improved automatic detection of various timestamp formats in CSV Importer
    * Automatic detection of case attributes and event attributes in CSV Importer
    * Removed unused fields in the Portal
    * Simplified import of process models
    * Multiple visual and performance improvements in custom dashboards


* **Bug Fix:**
    * Fixed issue with not being able to animate some logs
    * Fixed issue with misaligned timelines in the log animation
    * Fixed issue with CSV importer failing due to missing case identifiers or activity names
    * Fixed issue with the results of Similarity Search not being displayed until the Portal is refreshed
    * Fixed some issues with the Rework & repetition filter


##########################
Version 7.15
##########################

*Release Date: May, 2020*

* **Process Discoverer:** New ribbon interface makes it easier to tune and switch between visualization and abstraction settings
* **Dashboard:** Ability to create customized charts with user-defined KPIs
* **Portal:**
    * Enhanced user registration screen
    * Ability to choose file format when downloading event logs (XES or CSV, and encoding for CSV files)
* **Log Animation:** Visual improvements in the Log Animation
* **CSV Importer:** UI and performance improvements
* **Various bug fixes and performance improvements**



##########################
Version 7.14
##########################

*Release Date: March, 2020*

* **Process Discoverer:**
    * Re-engineered plugin with new internal, high-performing data structure
    * Re-designed user interface with new abstraction functionality and statistics visualization
* **Filter:**
    * Cosmetic improvements
    * Performance improvements
* **Dashboard:**
    * Log cloning feature
    * Cosmetic improvements
    * Performance improvements
* **Various bug fixes and performance improvements**



##########################
Version 7.13
##########################

*Release Date: February, 2020*

* **New modern UI featuring consistent branding and look & feel**
* **CSV Importer:**
    * Support for non UTF-8 encodings
    * Fault tolerance (e.g. missing attribute value)
* **Filter:**
    * New Rework & Repetition filter makes it easier to track cases with repeated tasks (e.g. rework due to amendments)
    * Ability to search for specific cases and event attributes when setting filters
    * New Case variant and Case ID Inspector view
* **Process Discoverer:**
    * Pie charts to show the percentage of cases, variants and events left after applying a filter
    * Performance improvements
* **Dashboard:**
    * Distinction between Case attributes and Event attributes
    * Relative frequency in Activities and Resources views
    * Performance improvements
* **Single Editor for process modeling based on BPMN.io (legacy editor deprecated)**
* **Various bug fixes**



##########################
Version 7.10
##########################

*Release Date: December, 2019*

* **Filter:**
    * Advanced case variant filter to show the distribution of case variants
    * Advanced options for the Eventually-follows filter
    * Filtering by processing time, waiting time and case utilization when events have start timestamps
    * Advanced options for Time window filters (case contained in the time window, active in, starts in, ends in)
    * Ability to download and upload filter criteria for reuse
    * Pie charts to show the percentage of cases, variants and events left after applying a filter
    * Minor cosmetic fixes
* **Dashboard:**
    * Support for case-level attributes
    * Minor cosmetic fixes
* **CSV Importer:**
    * Improved data type detection
    * Ability to import zipped and gzipped CSV files
* **Process Discoverer:** Various bug fixes and improvements
* **Caching mechanism to improve system performance**



##########################
Version 7.8
##########################

*Release Date: October, 2019*

* **Filter:** Advanced filtering options
* **CSV Importer:** More robust CSV Importer
* **Improved handling of security permissions for event logs**
* **Process Discoverer:**
    * Performance and visual improvements
    * Various bug fixes



##########################
Version 7.6
##########################

*Release Date: August, 2019*

* **Filter:** New Filter plugin
* **Process Discoverer:** Various bug fixes and performance and visual improvements
* **CSV Importer:** More robust CSV Importer
* **Improved handling of security permissions for event logs (Security button)**
* **Migrated to the current version of ZK libraries 8.6.0.1**
* **Dynamic switching of UI themes (Account -> Change theme)**



##########################
Version 7.5
##########################

*Release Date: August, 2019*

* **Dashboard:** New Dashboard plugin
* **Process Discoverer:**
    * Automatic centering and fit to screen when changing layout
    * Various bug fixes and performance improvements
* **CSV Importer:**
    * Improved tolerance for errors while importing CSVs
    * More robust mechanism to recognize timestamp format
    * Multiple UI improvements
* **Added password recovery feature**
