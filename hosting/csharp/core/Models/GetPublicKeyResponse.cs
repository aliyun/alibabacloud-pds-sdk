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
    public class GetPublicKeyResponse : TeaModel {
        /// <summary>
        /// App ID
        /// </summary>
        [NameInMap("app_id")]
        [Validation(Required=true)]
        public string AppId { get; set; }

        [NameInMap("key_pair_id")]
        [Validation(Required=false)]
        public string KeyPairId { get; set; }

        /// <summary>
        /// RSA加密算法的公钥, PEM格式
        /// </summary>
        [NameInMap("public_key")]
        [Validation(Required=true)]
        public string PublicKey { get; set; }

    }

}
