// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 
     */
    public class AddStoreResponse : TeaModel {
        /// <summary>
        /// 全球加速地址
        /// </summary>
        [NameInMap("accelerate_endpoint")]
        [Validation(Required=false)]
        public string AccelerateEndpoint { get; set; }

        /// <summary>
        /// 存储公共前缀
        /// </summary>
        [NameInMap("base_path")]
        [Validation(Required=false)]
        public string BasePath { get; set; }

        /// <summary>
        /// bucket名称
        /// </summary>
        [NameInMap("bucket")]
        [Validation(Required=true)]
        public string Bucket { get; set; }

        /// <summary>
        /// 内容分发地址
        /// </summary>
        [NameInMap("cdn_endpoint")]
        [Validation(Required=false)]
        public string CdnEndpoint { get; set; }

        /// <summary>
        /// 自定义全球加速地址
        /// </summary>
        [NameInMap("customized_accelerate_endpoint")]
        [Validation(Required=false)]
        public string CustomizedAccelerateEndpoint { get; set; }

        /// <summary>
        /// 自定义内容分发地址
        /// </summary>
        [NameInMap("customized_cdn_endpoint")]
        [Validation(Required=false)]
        public string CustomizedCdnEndpoint { get; set; }

        /// <summary>
        /// 自定义Public访问地址
        /// </summary>
        [NameInMap("customized_endpoint")]
        [Validation(Required=false)]
        public string CustomizedEndpoint { get; set; }

        /// <summary>
        /// 自定义vpc访问地址
        /// </summary>
        [NameInMap("customized_internal_endpoint")]
        [Validation(Required=false)]
        public string CustomizedInternalEndpoint { get; set; }

        /// <summary>
        /// domain ID
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=true)]
        public string DomainId { get; set; }

        /// <summary>
        /// Public访问地址
        /// </summary>
        [NameInMap("endpoint")]
        [Validation(Required=true)]
        public string Endpoint { get; set; }

        /// <summary>
        /// vpc访问地址
        /// </summary>
        [NameInMap("internal_endpoint")]
        [Validation(Required=false)]
        public string InternalEndpoint { get; set; }

        /// <summary>
        /// 地点
        /// </summary>
        [NameInMap("location")]
        [Validation(Required=false)]
        public string Location { get; set; }

        /// <summary>
        /// 存储归属，system表示系统提供，custom表示使用自己的存储
        /// </summary>
        [NameInMap("ownership")]
        [Validation(Required=true)]
        public string Ownership { get; set; }

        /// <summary>
        /// Policy授权,system类型store会将bucket权限授予当前云账号
        /// </summary>
        [NameInMap("policy")]
        [Validation(Required=true)]
        public string Policy { get; set; }

        /// <summary>
        /// 访问Bucket的角色ARN
        /// </summary>
        [NameInMap("role_arn")]
        [Validation(Required=false)]
        public string RoleArn { get; set; }

        /// <summary>
        /// store ID
        /// </summary>
        [NameInMap("store_id")]
        [Validation(Required=true)]
        public string StoreId { get; set; }

        /// <summary>
        /// 存储类型，当前只支持oss
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=true)]
        public string Type { get; set; }

    }

}
