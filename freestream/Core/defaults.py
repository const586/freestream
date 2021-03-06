﻿#Embedded file name: freestream\Core\defaults.pyo
import sys
import os
from simpledefs import *
DEFAULTPORT = 7760
SESSDEFAULTS_VERSION = 2
sessdefaults = {}
sessdefaults['version'] = SESSDEFAULTS_VERSION
sessdefaults['state_dir'] = None
sessdefaults['install_dir'] = u'.'
sessdefaults['ip'] = ''
sessdefaults['minport'] = DEFAULTPORT
sessdefaults['maxport'] = DEFAULTPORT
sessdefaults['random_port'] = 1
sessdefaults['bind'] = []
sessdefaults['ipv6_enabled'] = 0
sessdefaults['ipv6_binds_v4'] = None
sessdefaults['upnp_nat_access'] = UPNPMODE_UNIVERSAL_DIRECT
sessdefaults['timeout'] = 300.0
sessdefaults['timeout_check_interval'] = 60.0
sessdefaults['eckeypairfilename'] = None
sessdefaults['megacache'] = True
sessdefaults['overlay'] = True
sessdefaults['crawler'] = True
sessdefaults['buddycast'] = True
sessdefaults['magnetlink'] = True
sessdefaults['start_recommender'] = True
sessdefaults['download_help'] = True
sessdefaults['torrent_collecting'] = True
sessdefaults['superpeer'] = False
sessdefaults['overlay_log'] = None
sessdefaults['buddycast_interval'] = 15
sessdefaults['buddycast_max_peers'] = 2500
sessdefaults['torrent_collecting_max_torrents'] = 50000
sessdefaults['torrent_collecting_dir'] = None
sessdefaults['buffer_dir'] = None
sessdefaults['ads_dir'] = None
sessdefaults['torrent_collecting_rate'] = 50
sessdefaults['torrent_checking'] = 1
sessdefaults['torrent_checking_period'] = 31
sessdefaults['dialback'] = True
sessdefaults['dialback_active'] = True
sessdefaults['dialback_trust_superpeers'] = True
sessdefaults['socnet'] = True
sessdefaults['rquery'] = True
sessdefaults['stop_collecting_threshold'] = 200
sessdefaults['internaltracker'] = True
sessdefaults['nickname'] = '__default_name__'
sessdefaults['mugshot'] = None
sessdefaults['videoanalyserpath'] = None
sessdefaults['overlay_max_message_length'] = 8388608
sessdefaults['download_help_dir'] = None
sessdefaults['bartercast'] = True
sessdefaults['superpeer_file'] = None
sessdefaults['crawler_file'] = None
sessdefaults['buddycast_collecting_solution'] = BCCOLPOLICY_SIMPLE
sessdefaults['peer_icon_path'] = None
sessdefaults['stop_collecting_threshold'] = 200
sessdefaults['coopdlconfig'] = None
sessdefaults['family_filter'] = True
sessdefaults['nat_detect'] = True
sessdefaults['puncturing_internal_port'] = 6700
sessdefaults['stun_servers'] = [('stun1.tribler.org', 6701), ('stun2.tribler.org', 6702)]
sessdefaults['pingback_servers'] = [('pingback.tribler.org', 6703), ('pingback2.tribler.org', 6703)]
sessdefaults['live_aux_seeders'] = []
sessdefaults['mainline_dht'] = True
sessdefaults['multicast_local_peer_discovery'] = True
sessdefaults['votecast_recent_votes'] = 25
sessdefaults['votecast_random_votes'] = 25
sessdefaults['channelcast_recent_own_subscriptions'] = 13
sessdefaults['channelcast_random_own_subscriptions'] = 12
sessdefaults['dispersy'] = False
sessdefaults['dispersy_port'] = 6711
sessdefaults['ts_login'] = 'test'
sessdefaults['ts_password'] = 'test'
sessdefaults['authlevel'] = 0
sessdefaults['ts_user_key'] = ''
sessdefaults['max_socket_connects'] = 1000
sessdefaults['max_channel_query_results'] = 25
sessdefaults['subtitles_collecting'] = True
sessdefaults['subtitles_collecting_dir'] = None
sessdefaults['subtitles_upload_rate'] = 1024
sessdefaults['proxyservice_status'] = PROXYSERVICE_OFF
trackerdefaults = {}
trackerdefaults['tracker_url'] = None
trackerdefaults['tracker_dfile'] = None
trackerdefaults['tracker_dfile_format'] = ITRACKDBFORMAT_PICKLE
trackerdefaults['tracker_socket_timeout'] = 15
trackerdefaults['tracker_save_dfile_interval'] = 300
trackerdefaults['tracker_timeout_downloaders_interval'] = 2700
trackerdefaults['tracker_reannounce_interval'] = 1800
trackerdefaults['tracker_response_size'] = 50
trackerdefaults['tracker_timeout_check_interval'] = 5
trackerdefaults['tracker_nat_check'] = 3
trackerdefaults['tracker_log_nat_checks'] = 0
trackerdefaults['tracker_min_time_between_log_flushes'] = 3.0
trackerdefaults['tracker_min_time_between_cache_refreshes'] = 600.0
trackerdefaults['tracker_allowed_dir'] = None
trackerdefaults['tracker_allowed_list'] = ''
trackerdefaults['tracker_allowed_controls'] = 0
trackerdefaults['tracker_multitracker_enabled'] = 0
trackerdefaults['tracker_multitracker_allowed'] = ITRACKMULTI_ALLOW_AUTODETECT
trackerdefaults['tracker_multitracker_reannounce_interval'] = 120
trackerdefaults['tracker_multitracker_maxpeers'] = 20
trackerdefaults['tracker_aggregate_forward'] = [None, None]
trackerdefaults['tracker_aggregator'] = 0
trackerdefaults['tracker_hupmonitor'] = 0
trackerdefaults['tracker_multitracker_http_timeout'] = 60
trackerdefaults['tracker_parse_dir_interval'] = 60
trackerdefaults['tracker_show_infopage'] = 1
trackerdefaults['tracker_infopage_redirect'] = None
trackerdefaults['tracker_show_names'] = 1
trackerdefaults['tracker_favicon'] = None
trackerdefaults['tracker_allowed_ips'] = []
trackerdefaults['tracker_banned_ips'] = []
trackerdefaults['tracker_only_local_override_ip'] = ITRACK_IGNORE_ANNOUNCEIP_IFNONATCHECK
trackerdefaults['tracker_logfile'] = None
trackerdefaults['tracker_allow_get'] = 1
trackerdefaults['tracker_keep_dead'] = 0
trackerdefaults['tracker_scrape_allowed'] = ITRACKSCRAPE_ALLOW_FULL
sessdefaults.update(trackerdefaults)
DLDEFAULTS_VERSION = 3
dldefaults = {}
dldefaults['version'] = DLDEFAULTS_VERSION
dldefaults['max_uploads'] = 7
dldefaults['keepalive_interval'] = 120.0
dldefaults['download_slice_size'] = 16384
dldefaults['upload_unit_size'] = 1460
dldefaults['request_backlog'] = 10
dldefaults['max_message_length'] = 8388608
dldefaults['selector_enabled'] = 1
dldefaults['expire_cache_data'] = 10
dldefaults['priority'] = []
dldefaults['saveas'] = None
dldefaults['saveas_filename'] = None
dldefaults['max_slice_length'] = 131072
dldefaults['max_rate_period'] = 20.0
dldefaults['upload_rate_fudge'] = 5.0
dldefaults['tcp_ack_fudge'] = 0.03
dldefaults['rerequest_interval'] = 300
dldefaults['min_peers'] = 20
dldefaults['http_timeout'] = 60
dldefaults['max_initiate'] = 40
dldefaults['check_hashes'] = 1
dldefaults['max_upload_rate'] = 0
dldefaults['max_download_rate'] = 0
if sys.platform == 'win32':
    dldefaults['alloc_type'] = DISKALLOC_NORMAL
else:
    dldefaults['alloc_type'] = DISKALLOC_SPARSE
dldefaults['alloc_rate'] = 2.0
dldefaults['buffer_reads'] = 0
dldefaults['write_buffer_size'] = 4
dldefaults['breakup_seed_bitfield'] = 1
dldefaults['snub_time'] = 30.0
dldefaults['rarest_first_cutoff'] = 2
dldefaults['rarest_first_priority_cutoff'] = 5
dldefaults['min_uploads'] = 4
dldefaults['max_files_open'] = 50
dldefaults['round_robin_period'] = 30
dldefaults['super_seeder'] = 0
dldefaults['security'] = 1
dldefaults['max_connections'] = 0
dldefaults['auto_kick'] = 1
dldefaults['double_check'] = 0
dldefaults['triple_check'] = 0
dldefaults['lock_files'] = 0
dldefaults['lock_while_reading'] = 0
dldefaults['auto_flush'] = 0
dldefaults['coopdl_role'] = COOPDL_ROLE_COORDINATOR
dldefaults['coopdl_coordinator_permid'] = ''
dldefaults['proxy_mode'] = PROXY_MODE_OFF
dldefaults['max_helpers'] = 10
dldefaults['exclude_ips'] = ''
dldefaults['mode'] = 0
dldefaults['vod_usercallback'] = None
dldefaults['vod_userevents'] = []
dldefaults['video_source'] = None
dldefaults['video_ratelimit'] = 0
dldefaults['video_source_authconfig'] = None
dldefaults['selected_files'] = []
dldefaults['ut_pex_max_addrs_from_peer'] = 50
dldefaults['extra_files'] = []
dldefaults['auto_download_limit'] = False
dldefaults['wait_sufficient_speed'] = False
dldefaults['enable_http_support'] = True
dldefaults['player_buffer_time'] = 5
dldefaults['live_buffer_time'] = 10
dldefaults['download_finished_callback'] = None
dldefaults['download_failed_callback'] = None
dldefaults['direct_download_url'] = None
dldefaults['predownload'] = False
dldefaults['same_nat_try_internal'] = 0
dldefaults['unchoke_bias_for_internal'] = 0
tdefdictdefaults = {}
tdefdictdefaults['comment'] = None
tdefdictdefaults['created by'] = None
tdefdictdefaults['announce'] = None
tdefdictdefaults['announce-list'] = None
tdefdictdefaults['nodes'] = None
tdefdictdefaults['httpseeds'] = None
tdefdictdefaults['url-list'] = None
tdefdictdefaults['encoding'] = None
tdefmetadefaults = {}
tdefmetadefaults['version'] = 1
tdefmetadefaults['piece length'] = 0
tdefmetadefaults['makehash_md5'] = 0
tdefmetadefaults['makehash_crc32'] = 0
tdefmetadefaults['makehash_sha1'] = 0
tdefmetadefaults['createmerkletorrent'] = 0
tdefmetadefaults['torrentsigkeypairfilename'] = None
tdefmetadefaults['thumb'] = None
tdefdefaults = {}
tdefdefaults.update(tdefdictdefaults)
tdefdefaults.update(tdefmetadefaults)
