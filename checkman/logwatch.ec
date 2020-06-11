title: Forward Logwatch Messages to the Event Console
agents: linux, windows, aix, solaris
catalog: os/files
license: GPL
distribution: check_mk
description:
 This check processes the output of agents with the logwatch plugin. The windows agent has built
 in this extension. Per default this check forwards any data to the Checkmk Event Console.
 With additional configuration the messages can be reclassified to a different state via
 logwatch patterns before they are forwarded to the Event Console.

inventory:
 One service {"Log Forwarding"} is created on each host when the option
 {logwatch_forward_to_ec} is set to {True}.

