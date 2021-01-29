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
    public class AddStoreRequest : TeaModel {
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
        [Validation(Required=false)]
        public string Bucket { get; set; }

        /// <summary>
        /// domain ID
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=true)]
        public string DomainId { get; set; }

        /// <summary>
        /// 存储访问地址
        /// </summary>
        [NameInMap("endpoint")]
        [Validation(Required=true)]
        public string Endpoint { get; set; }

        /// <summary>
        /// 存储归属，system表示系统提供，custom表示使用自己的存储
        /// </summary>
        [NameInMap("ownership")]
        [Validation(Required=false)]
        public string Ownership { get; set; }

        /// <summary>
        /// 访问Bucket的角色ARN
        /// </summary>
        [NameInMap("role_arn")]
        [Validation(Required=false)]
        public string RoleArn { get; set; }

        /// <summary>
        /// 存储类型，当前只支持oss
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=true)]
        public string Type { get; set; }

    }

}
