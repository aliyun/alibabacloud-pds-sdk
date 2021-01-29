// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * update domain request
     */
    public class UpdateDomainRequest : TeaModel {
        [NameInMap("auth_config")]
        [Validation(Required=false)]
        public Dictionary<string, object> AuthConfig { get; set; }

        /// <summary>
        /// 钉钉 App Id
        /// </summary>
        [NameInMap("auth_dingding_app_id")]
        [Validation(Required=false)]
        public string AuthDingdingAppId { get; set; }

        /// <summary>
        /// 钉钉 App Secret
        /// </summary>
        [NameInMap("auth_dingding_app_secret")]
        [Validation(Required=false)]
        public string AuthDingdingAppSecret { get; set; }

        /// <summary>
        /// 启用钉钉认证
        /// </summary>
        [NameInMap("auth_dingding_enable")]
        [Validation(Required=false)]
        public bool? AuthDingdingEnable { get; set; }

        [NameInMap("auth_endpoint_enable")]
        [Validation(Required=false)]
        public bool? AuthEndpointEnable { get; set; }

        /// <summary>
        /// RAM App Id
        /// </summary>
        [NameInMap("auth_ram_app_id")]
        [Validation(Required=false)]
        public string AuthRamAppId { get; set; }

        /// <summary>
        /// RAM App Secret
        /// </summary>
        [NameInMap("auth_ram_app_secret")]
        [Validation(Required=false)]
        public string AuthRamAppSecret { get; set; }

        /// <summary>
        /// 启用 RAM 认证
        /// </summary>
        [NameInMap("auth_ram_enable")]
        [Validation(Required=false)]
        public bool? AuthRamEnable { get; set; }

        /// <summary>
        /// 数据 Hash 算法
        /// </summary>
        [NameInMap("data_hash_name")]
        [Validation(Required=false)]
        public string DataHashName { get; set; }

        /// <summary>
        /// Domain 描述
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=false)]
        public string Description { get; set; }

        /// <summary>
        /// Domain ID
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=true)]
        public string DomainId { get; set; }

        /// <summary>
        /// Domain 名称
        /// </summary>
        [NameInMap("domain_name")]
        [Validation(Required=false)]
        public string DomainName { get; set; }

        /// <summary>
        /// 事件通知 MNS 匹配文件名
        /// </summary>
        [NameInMap("event_filename_matches")]
        [Validation(Required=false)]
        public string EventFilenameMatches { get; set; }

        /// <summary>
        /// 事件通知 MNS Endpoint
        /// </summary>
        [NameInMap("event_mns_endpoint")]
        [Validation(Required=false)]
        public string EventMnsEndpoint { get; set; }

        /// <summary>
        /// 事件通知 MNS Topic
        /// </summary>
        [NameInMap("event_mns_topic")]
        [Validation(Required=false)]
        public string EventMnsTopic { get; set; }

        /// <summary>
        /// 事件名列表
        /// </summary>
        [NameInMap("event_names")]
        [Validation(Required=false)]
        public List<string> EventNames { get; set; }

        /// <summary>
        /// 事件通知 Role Arn
        /// </summary>
        [NameInMap("event_role_arn")]
        [Validation(Required=false)]
        public string EventRoleArn { get; set; }

        /// <summary>
        /// 开启自动初始化 Drive
        /// </summary>
        [NameInMap("init_drive_enable")]
        [Validation(Required=false)]
        public bool? InitDriveEnable { get; set; }

        /// <summary>
        /// 自动初始化 Drive 大小
        /// </summary>
        [NameInMap("init_drive_size")]
        [Validation(Required=false)]
        public long? InitDriveSize { get; set; }

        /// <summary>
        /// 自动初始化 Drive 使用 Store ID
        /// </summary>
        [NameInMap("init_drive_store_id")]
        [Validation(Required=false)]
        public string InitDriveStoreId { get; set; }

        [NameInMap("published_app_access_strategy")]
        [Validation(Required=false)]
        public AppAccessStrategy PublishedAppAccessStrategy { get; set; }

        /// <summary>
        /// 开启分享
        /// </summary>
        [NameInMap("sharable")]
        [Validation(Required=false)]
        public bool? Sharable { get; set; }

    }

}
