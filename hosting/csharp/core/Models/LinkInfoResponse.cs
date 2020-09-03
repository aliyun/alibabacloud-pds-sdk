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
    public class LinkInfoResponse : TeaModel {
        /// <summary>
        /// 认证类型
        /// </summary>
        [NameInMap("authentication_type")]
        [Validation(Required=true)]
        public string AuthenticationType { get; set; }

        /// <summary>
        /// 创建时间
        /// </summary>
        [NameInMap("created_at")]
        [Validation(Required=true)]
        public long CreatedAt { get; set; }

        /// <summary>
        /// Domain ID
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=true)]
        public string DomainId { get; set; }

        /// <summary>
        /// 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        /// </summary>
        [NameInMap("extra")]
        [Validation(Required=false)]
        public string Extra { get; set; }

        /// <summary>
        /// 唯一身份标识
        /// </summary>
        [NameInMap("identity")]
        [Validation(Required=true)]
        public string Identity { get; set; }

        /// <summary>
        /// 最后登录时间
        /// </summary>
        [NameInMap("last_login_time")]
        [Validation(Required=true)]
        public long LastLoginTime { get; set; }

        /// <summary>
        /// 状态
        /// </summary>
        [NameInMap("status")]
        [Validation(Required=true)]
        public string Status { get; set; }

        /// <summary>
        /// 用户ID
        /// </summary>
        [NameInMap("user_id")]
        [Validation(Required=true)]
        public string UserId { get; set; }

    }

}
