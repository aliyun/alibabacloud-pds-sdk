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
    public class VerifyTokenResponse : TeaModel {
        /// <summary>
        /// 实人认证的Token
        /// </summary>
        [NameInMap("token")]
        [Validation(Required=true)]
        public string Token { get; set; }

        /// <summary>
        /// 实人认证token有效秒数，如1800
        /// </summary>
        [NameInMap("ttl")]
        [Validation(Required=true)]
        public long? Ttl { get; set; }

        /// <summary>
        /// 实人认证的URL，包含Token
        /// </summary>
        [NameInMap("url")]
        [Validation(Required=true)]
        public string Url { get; set; }

    }

}
