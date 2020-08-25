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
    public class UserAuthentication : TeaModel {
        /// <summary>
        /// 认证类型
        /// </summary>
        [NameInMap("AuthenticationType")]
        [Validation(Required=true)]
        public string AuthenticationType { get; set; }

        /// <summary>
        /// 创建时间
        /// </summary>
        [NameInMap("CreatedAt")]
        [Validation(Required=true)]
        public long CreatedAt { get; set; }

        /// <summary>
        /// 详情
        /// </summary>
        [NameInMap("Detail")]
        [Validation(Required=true)]
        public string Detail { get; set; }

        /// <summary>
        /// Domain ID
        /// </summary>
        [NameInMap("DomainID")]
        [Validation(Required=true)]
        public string DomainID { get; set; }

        /// <summary>
        /// 唯一身份标识
        /// </summary>
        [NameInMap("Identity")]
        [Validation(Required=true)]
        public string Identity { get; set; }

        /// <summary>
        /// 最后登录时间
        /// </summary>
        [NameInMap("LastLoginTime")]
        [Validation(Required=true)]
        public long LastLoginTime { get; set; }

        /// <summary>
        /// 状态
        /// </summary>
        [NameInMap("Status")]
        [Validation(Required=true)]
        public string Status { get; set; }

        /// <summary>
        /// 用户ID
        /// </summary>
        [NameInMap("UserID")]
        [Validation(Required=true)]
        public string UserID { get; set; }

        /// <summary>
        /// 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        /// </summary>
        [NameInMap("extra")]
        [Validation(Required=false)]
        public string Extra { get; set; }

    }

}
