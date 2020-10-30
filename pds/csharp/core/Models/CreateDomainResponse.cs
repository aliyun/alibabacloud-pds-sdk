// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * create domain response
     */
    public class CreateDomainResponse : TeaModel {
        /// <summary>
        /// Domain CName
        /// </summary>
        [NameInMap("api_cname")]
        [Validation(Required=false)]
        public string ApiCname { get; set; }

        /// <summary>
        /// 支付宝 App Id
        /// </summary>
        [NameInMap("auth_alipay_app_id")]
        [Validation(Required=false)]
        public string AuthAlipayAppId { get; set; }

        /// <summary>
        /// 是否开启了支付宝认证
        /// </summary>
        [NameInMap("auth_alipay_enable")]
        [Validation(Required=false)]
        public bool? AuthAlipayEnable { get; set; }

        /// <summary>
        /// 支付宝 App Secret
        /// </summary>
        [NameInMap("auth_alipay_private_key")]
        [Validation(Required=false)]
        public string AuthAlipayPrivateKey { get; set; }

        /// <summary>
        /// 登录相关信息
        /// </summary>
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
        /// 是否开启了钉钉认证
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
        /// 是否开启了 RAM 认证
        /// </summary>
        [NameInMap("auth_ram_enable")]
        [Validation(Required=false)]
        public bool? AuthRamEnable { get; set; }

        /// <summary>
        /// Domain 创建时间
        /// </summary>
        [NameInMap("created_at")]
        [Validation(Required=false)]
        public string CreatedAt { get; set; }

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
        [Validation(Required=false)]
        public string DomainId { get; set; }

        /// <summary>
        /// Domain 描述
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
        /// 是否开启了自动初始化 Drive
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
        /// 自动初始化 Drive 所用 Store ID
        /// </summary>
        [NameInMap("init_drive_store_id")]
        [Validation(Required=false)]
        public string InitDriveStoreId { get; set; }

        /// <summary>
        /// Domain 类型
        /// </summary>
        [NameInMap("mode")]
        [Validation(Required=false)]
        public string Mode { get; set; }

        /// <summary>
        /// Domain 类型
        /// </summary>
        [NameInMap("path_type")]
        [Validation(Required=false)]
        public string PathType { get; set; }

        [NameInMap("published_app_access_strategy")]
        [Validation(Required=false)]
        public AppAccessStrategy PublishedAppAccessStrategy { get; set; }

        /// <summary>
        /// 是否开启了分享
        /// </summary>
        [NameInMap("sharable")]
        [Validation(Required=false)]
        public bool? Sharable { get; set; }

        /// <summary>
        /// 存储级别
        /// </summary>
        [NameInMap("store_level")]
        [Validation(Required=false)]
        public string StoreLevel { get; set; }

        /// <summary>
        /// 存储 Region 列表
        /// </summary>
        [NameInMap("store_region_list")]
        [Validation(Required=false)]
        public List<string> StoreRegionList { get; set; }

        /// <summary>
        /// Domain 更新时间
        /// </summary>
        [NameInMap("updated_at")]
        [Validation(Required=false)]
        public string UpdatedAt { get; set; }

    }

}
