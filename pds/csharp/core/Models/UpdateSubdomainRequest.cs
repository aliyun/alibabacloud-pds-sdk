// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class UpdateSubdomainRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// 描述
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=false)]
        public string Description { get; set; }

        /// <summary>
        /// 名称
        /// </summary>
        [NameInMap("name")]
        [Validation(Required=false)]
        public string Name { get; set; }

        /// <summary>
        /// 用以唯一标识subdomain
        /// </summary>
        [NameInMap("subdomain_id")]
        [Validation(Required=true)]
        public string SubdomainId { get; set; }

        /// <summary>
        /// 逻辑空间quota，-1表示无限制，单位为字节
        /// </summary>
        [NameInMap("total_size")]
        [Validation(Required=false)]
        public long? TotalSize { get; set; }

        /// <summary>
        /// 用户数quota，-1表示无限制
        /// </summary>
        [NameInMap("user_quota")]
        [Validation(Required=false)]
        public long? UserQuota { get; set; }

    }

}
