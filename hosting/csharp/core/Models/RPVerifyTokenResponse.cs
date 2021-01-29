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
    public class RPVerifyTokenResponse : TeaModel {
        /// <summary>
        /// 是否需要实人认证，如果用户已通过认证，或者未开启实人认证，返回false
        /// </summary>
        [NameInMap("need_rp_verify")]
        [Validation(Required=true)]
        public bool? NeedRpVerify { get; set; }

        [NameInMap("verify_token")]
        [Validation(Required=true)]
        public VerifyTokenResponse VerifyToken { get; set; }

    }

}
