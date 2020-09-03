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
    public class VerifyCodeResponse : TeaModel {
        /// <summary>
        /// 修改密码的临时授权码
        /// </summary>
        [NameInMap("state")]
        [Validation(Required=true)]
        public string State { get; set; }

    }

}
