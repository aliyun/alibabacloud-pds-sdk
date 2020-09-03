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
    public class GetAccessTokenByLinkInfoRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

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
        /// 认证类型
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=true)]
        public string Type { get; set; }

    }

}
