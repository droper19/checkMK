import pytest

# Triggers plugin loading of plugins.wato which registers all the plugins
import cmk.gui.wato  # pylint: disable=unused-import
import cmk.gui.watolib as watolib
from cmk.gui.valuespec import ValueSpec
from cmk.gui.plugins.watolib.utils import (
    config_variable_group_registry,
    ConfigVariableGroup,
    ConfigDomain,
    config_variable_registry,
    configvar_order,
)


def test_registered_ac_tests():
    registered_plugins = sorted(watolib.ac_test_registry.keys())
    assert registered_plugins == sorted([
        'ACTestAlertHandlerEventTypes',
        'ACTestApacheNumberOfProcesses',
        'ACTestApacheProcessUsage',
        'ACTestBackupConfigured',
        'ACTestBackupNotEncryptedConfigured',
        'ACTestCheckMKHelperUsage',
        'ACTestESXDatasources',
        'ACTestGenericCheckHelperUsage',
        'ACTestHTTPSecured',
        'ACTestLDAPSecured',
        'ACTestLiveproxyd',
        'ACTestLivestatusUsage',
        'ACTestNumberOfUsers',
        'ACTestOldDefaultCredentials',
        'ACTestPersistentConnections',
        'ACTestRulebasedNotifications',
        'ACTestSecureAgentUpdaterTransport',
        'ACTestSecureNotificationSpoolerMessages',
        'ACTestSizeOfExtensions',
        'ACTestTmpfs',
    ])


def test_registered_config_domains():
    registered = sorted(watolib.config_domain_registry.keys())
    assert registered == sorted([
        'apache',
        'ca-certificates',
        'check_mk',
        'dcd',
        'diskspace',
        'ec',
        'liveproxyd',
        'mknotifyd',
        'multisite',
        'omd',
        'rrdcached',
    ])


def test_registered_automation_commands():
    registered = sorted(watolib.automation_command_registry.keys())
    assert registered == sorted([
        'activate-changes',
        'check-analyze-config',
        'execute-dcd-command',
        'network-scan',
        'push-snapshot',
    ])


def test_registered_configvars():
    registered = sorted(config_variable_registry.keys())
    assert registered == sorted([
        'actions',
        'adhoc_downtime',
        'agent_deployment_enabled',
        'agent_deployment_host_selection',
        'agent_simulator',
        'alert_handler_event_types',
        'alert_handler_timeout',
        'alert_logging',
        'apache_process_tuning',
        'archive_orphans',
        'auth_by_http_header',
        'bake_agents_on_restart',
        'builtin_icon_visibility',
        'bulk_discovery_default_settings',
        'check_mk_perfdata_with_times',
        'cluster_max_cachefile_age',
        'cmc_authorization',
        'cmc_check_helpers',
        'cmc_check_timeout',
        'cmc_cmk_helpers',
        'cmc_debug_notifications',
        'cmc_dump_core',
        'cmc_flap_settings',
        'cmc_graphite',
        'cmc_import_nagios_state',
        'cmc_initial_scheduling',
        'cmc_livestatus_lines_per_file',
        'cmc_livestatus_logcache_size',
        'cmc_livestatus_threads',
        'cmc_log_cmk_helpers',
        'cmc_log_levels',
        'cmc_log_limit',
        'cmc_log_microtime',
        'cmc_log_rotation_method',
        'cmc_log_rrdcreation',
        'cmc_pnp_update_delay',
        'cmc_pnp_update_on_restart',
        'cmc_real_time_checks',
        'cmc_real_time_helpers',
        'cmc_smartping_tuning',
        'cmc_state_retention_interval',
        'cmc_statehist_cache',
        'cmc_timeperiod_horizon',
        'config',
        'context_buttons_to_show',
        'crash_report_target',
        'dcd_log_levels',
        'dcd_web_api_connection',
        'debug',
        'debug_livestatus_queries',
        'debug_rules',
        'default_user_profile',
        'delay_precompile',
        'diskspace_cleanup',
        'enable_rulebased_notifications',
        'enable_sounds',
        'escape_plugin_output',
        'event_limit',
        'eventsocket_queue_len',
        'failed_notification_horizon',
        'graph_timeranges',
        'hard_query_limit',
        'history_lifetime',
        'history_rotation',
        'hostname_translation',
        'housekeeping_interval',
        'inventory_check_autotrigger',
        'inventory_check_do_scan',
        'inventory_check_interval',
        'inventory_check_severity',
        'liveproxyd_default_connection_params',
        'liveproxyd_log_levels',
        'lock_on_logon_failures',
        'log_level',
        'log_levels',
        'log_messages',
        'log_rulehits',
        'login_screen',
        'mkeventd_connect_timeout',
        'mkeventd_notify_contactgroup',
        'mkeventd_notify_facility',
        'mkeventd_notify_remotehost',
        'mkeventd_pprint_rules',
        'mkeventd_service_levels',
        'mknotifyd_insecure_message_format',
        'multisite_draw_ruleicon',
        'notification_backlog',
        'notification_bulk_interval',
        'notification_fallback_email',
        'notification_logging',
        'notification_plugin_timeout',
        'notification_spooling',
        'page_heading',
        'pagetitle_date_format',
        'password_policy',
        'piggyback_max_cachefile_age',
        'profile',
        'quicksearch_dropdown_limit',
        'quicksearch_search_order',
        'record_inline_snmp_stats',
        'remote_status',
        'replication',
        'reporting_date_format',
        'reporting_email_options',
        'reporting_filename',
        'reporting_font_family',
        'reporting_font_size',
        'reporting_graph_layout',
        'reporting_lineheight',
        'reporting_margins',
        'reporting_mirror_margins',
        'reporting_pagesize',
        'reporting_rangespec',
        'reporting_table_layout',
        'reporting_time_format',
        'reporting_use',
        'reporting_view_limit',
        'reschedule_timeout',
        'restart_locking',
        'retention_interval',
        'rrdcached_tuning',
        'rule_optimizer',
        'save_user_access_times',
        'selection_livetime',
        'service_view_grouping',
        'show_livestatus_errors',
        'sidebar_notify_interval',
        'sidebar_show_version_in_sidebar',
        'sidebar_update_interval',
        'simulation_mode',
        'single_user_session',
        'site_autostart',
        'site_core',
        'site_liveproxyd',
        'site_livestatus_tcp',
        'site_mkeventd',
        'site_nsca',
        'snmp_credentials',
        'socket_queue_len',
        'soft_query_limit',
        'staleness_threshold',
        'start_url',
        'statistics_interval',
        'table_row_limit',
        'tcp_connect_timeout',
        'topology_default_filter_group',
        'translate_snmptraps',
        'trusted_certificate_authorities',
        'ui_theme',
        'use_dns_cache',
        'use_inline_snmp',
        'use_new_descriptions_for',
        'user_downtime_timeranges',
        'user_icons_and_actions',
        'user_idle_timeout',
        'user_localizations',
        'view_action_defaults',
        'virtual_host_trees',
        'wato_activation_method',
        'wato_hide_filenames',
        'wato_hide_folders_without_read_permissions',
        'wato_hide_help_in_lists',
        'wato_hide_hosttags',
        'wato_hide_varnames',
        'wato_icon_categories',
        'wato_legacy_eval',
        'wato_max_snapshots',
        'wato_pprint_config',
        'wato_upload_insecure_snapshots',
        'wato_use_git',
    ])


# Can be removed once we use mypy there
def test_registered_configvars_types():
    for var_class in config_variable_registry.values():
        var = var_class()
        assert issubclass(var.group(), ConfigVariableGroup)
        assert issubclass(var.domain(), ConfigDomain)
        assert isinstance(var.ident(), str)
        assert isinstance(var.valuespec(), ValueSpec)


def test_registered_configvar_groups():
    registered = sorted(config_variable_group_registry.keys())
    assert registered == sorted([
        u'Administration Tool (WATO)',
        u'Alert Handlers',
        u'Automatic agent updates',
        u'Dynamic Configuration',
        u'Event Console: Generic',
        u'Event Console: Logging & Diagnose',
        u'Event Console: SNMP traps',
        u'Execution of checks',
        u'Livestatus Proxy',
        u'Monitoring Core',
        u'Notifications',
        u'Reporting',
        u'Service discovery',
        u'Site Management',
        u'User Interface',
        u'User Management',
    ])


def test_legacy_configvar_order_access():
    with pytest.raises(NotImplementedError) as e:
        configvar_order()["x"] = 10
    assert "werk #6911" in "%s" % e


def test_registered_rulespec_groups():
    registered = sorted(watolib.rulespec_group_registry.keys())
    assert registered == sorted([
        'activechecks',
        'agent',
        'agents',
        'checkparams',
        'datasource_programs',
        'eventconsole',
        'grouping',
        'inventory',
        'monconf',
        'static',
        'user_interface',
    ])


def test_legacy_register_rulegroup(monkeypatch):
    monkeypatch.setattr(watolib, "rulespec_group_registry", watolib.RulespecGroupRegistry())
    watolib.register_rulegroup("abc", "A B C", "abc 123")

    group = watolib.get_rulegroup("abc")
    assert isinstance(group, watolib.RulespecGroup)
    assert group.name == "abc"
    assert group.title == "A B C"
    assert group.help == "abc 123"


def test_legacy_get_not_existing_rulegroup(monkeypatch):
    monkeypatch.setattr(watolib, "rulespec_group_registry", watolib.RulespecGroupRegistry())

    group = watolib.get_rulegroup("xyz")
    assert isinstance(group, watolib.RulespecGroup)
    assert group.name == "xyz"
    assert group.title == "xyz"
    assert group.help is None


@pytest.mark.parametrize("mode,result", [
    ("rulesets", [
        ('activechecks', u'Active checks (HTTP, TCP, etc.)'),
        ('agent', u'Access to Agents'),
        ('agents', u'Monitoring Agents'),
        ('checkparams', u'Parameters for discovered services'),
        ('datasource_programs', u'Datasource Programs'),
        ('eventconsole', u'Event Console'),
        ('grouping', u'Grouping'),
        ('inventory', u'Hardware/Software-Inventory'),
        ('monconf', u'Monitoring Configuration'),
        ('user_interface', u'User Interface'),
    ]),
    ("static_checks", [
        ('static', 'Manual Checks'),
    ]),
])
def test_rulespec_group_choices(mode, result, monkeypatch):
    monkeypatch.setattr(watolib.Rulespecs, "get_main_groups",
                        lambda self: watolib.rulespec_group_registry.keys())

    rulespecs = watolib.Rulespecs()
    assert sorted(rulespecs.get_group_choices(mode=mode)) == sorted(result)
