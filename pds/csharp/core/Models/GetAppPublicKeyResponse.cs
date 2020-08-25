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
    public class GetAppPublicKeyResponse : TeaModel {
        /// <summary>
        /// App ID
        /// </summary>
        [NameInMap("app_id")]
        [Validation(Required=true)]
        public string AppId { get; set; }

        /// <summary>
        /// RSA加密算法的公钥, PEM格式
        /// </summary>
        [NameInMap("public_key")]
        [Validation(Required=true)]
        public string PublicKey { get; set; }

    }

}
