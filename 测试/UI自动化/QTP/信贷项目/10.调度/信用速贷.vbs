Set qtApp = CreateObject("QuickTest.Application") ' Create the Application object
qtApp.Launch ' Start UFT
qtApp.Visible = True ' Make the UFT application visible
qtApp.ShowPaneScreen "ActiveScreen", True
qtApp.WindowState = "Maximized" 'rem--��󻯴���

' Set UFT run options
qtApp.Options.Run.ImageCaptureForTestResults="OnError"'rem--�����ͼ

qtApp.Options.Run.RunMode="Fast"'rem--��������ģʽ
qtApp.Options.Run.ViewResults=False'rem--���н�����չʾ���Ա���

qtApp.Open "../01.���Խű�/���Խű�����",True 'rem--Open the test in read-only modeֻ����ʽ�򿪲��Խű�

Set qtTest = qtApp.Test'rem--set run settings for the test
qtTest.Environment("FileName")="�����ٴ�����"
qtTest.Environment("PublicScript")="�����ٴ���build��"
qtTest.Settings.Run.IterationMode="rngAll" 'rem--����ʱ����������
qtTest.Settings.Run.OnError = "Stop" 'rem--'Instruct UFT to Stop when error occurs

Set qtResultsOpt = CreateObject("QuickTest.RunResultsOptions") ' Create the Run Results Options object
qtResultsOpt.ResultsLocation = "..\\09.���Ա���\\Res1" ' Set the results location

'Set options for automatic export of run results at the end of every run session

Set qtAutoExportResultsOpts = qtApp.Options.Run.AutoExportReportConfig
qtAutoExportResultsOpts.AutoExportResults = True ' Instruct UFT to automatically export the run results at the end of each run session
qtAutoExportResultsOpts.StepDetailsReport = True ' Instruct UFT to automatically export the step details part of the run results at the end of each run session
qtAutoExportResultsOpts.DataTableReport = True ' Instruct UFT to automatically export the data table part of the run results at the end of each run session
qtAutoExportResultsOpts.LogTrackingReport = True ' Instruct UFT to automatically export the log tracking part of the run results at the end of each run session
qtAutoExportResultsOpts.ScreenRecorderReport = True ' Instruct UFT to automatically export the screen recorder part of the run results at the end of each run session
qtAutoExportResultsOpts.SystemMonitorReport = False ' Instruct UFT not to automatically export the system monitor part of the run results at the end of each run session
qtAutoExportResultsOpts.ExportLocation = "..\\09.���Ա���" 'Instruct UFT to automatically export the run results to the Desktop at the end of each run session
qtAutoExportResultsOpts.UserDefinedXSL = "..\\09.���Ա���\\MyCustXSL.xsl" ' Specify the customized XSL file when exporting the run results data
qtAutoExportResultsOpts.StepDetailsReportFormat = "UserDefined" ' Instruct UFT to use a customized XSL file when exporting the run results data
qtAutoExportResultsOpts.ExportForFailedRunsOnly = True ' Instruct UFT to automatically export run results only for failed runs

qtTest.Run qtResultsOpt ' Run the test���в��ԣ�����洢��qtResultsOpt·��

MsgBox qtTest.LastRunResults.Status ' Check the results of the test run
'qtTest.Close ' Close the test

qtApp.quit

Set qtResultsOpt = Nothing ' Release the Run Results Options object
Set qtTest = Nothing ' Release the Test object
Set qtApp = Nothing ' Release the Application object
Set qtAutoExportResultsOpts = Nothing 
