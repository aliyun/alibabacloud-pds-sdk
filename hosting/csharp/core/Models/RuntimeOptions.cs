/**
 *
 */
// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    public class RuntimeOptions : TeaModel {
        /// <summary>
        /// whether to try again
        /// </summary>
        [NameInMap("autoretry")]
        [Validation(Required=false)]
        public bool? Autoretry { get; set; }

        /// <summary>
        /// ignore SSL validation
        /// </summary>
        [NameInMap("ignoreSSL")]
        [Validation(Required=false)]
        public bool? IgnoreSSL { get; set; }

        /// <summary>
        /// maximum number of retries
        /// </summary>
        [NameInMap("maxAttempts")]
        [Validation(Required=false)]
        public int? MaxAttempts { get; set; }

        /// <summary>
        /// backoff policy
        /// </summary>
        [NameInMap("backoffPolicy")]
        [Validation(Required=false)]
        public string BackoffPolicy { get; set; }

        /// <summary>
        /// backoff period
        /// </summary>
        [NameInMap("backoffPeriod")]
        [Validation(Required=false)]
        public int? BackoffPeriod { get; set; }

        /// <summary>
        /// read timeout
        /// </summary>
        [NameInMap("readTimeout")]
        [Validation(Required=false)]
        public int? ReadTimeout { get; set; }

        /// <summary>
        /// connect timeout
        /// </summary>
        [NameInMap("connectTimeout")]
        [Validation(Required=false)]
        public int? ConnectTimeout { get; set; }

        /// <summary>
        /// http proxy url
        /// </summary>
        [NameInMap("httpProxy")]
        [Validation(Required=false)]
        public string HttpProxy { get; set; }

        /// <summary>
        /// https Proxy url
        /// </summary>
        [NameInMap("httpsProxy")]
        [Validation(Required=false)]
        public string HttpsProxy { get; set; }

        /// <summary>
        /// agent blacklist
        /// </summary>
        [NameInMap("noProxy")]
        [Validation(Required=false)]
        public string NoProxy { get; set; }

        /// <summary>
        /// maximum number of connections
        /// </summary>
        [NameInMap("maxIdleConns")]
        [Validation(Required=false)]
        public int? MaxIdleConns { get; set; }

        /// <summary>
        /// local addr
        /// </summary>
        [NameInMap("localAddr")]
        [Validation(Required=false)]
        public string LocalAddr { get; set; }

        /// <summary>
        /// SOCKS5 proxy
        /// </summary>
        [NameInMap("socks5Proxy")]
        [Validation(Required=false)]
        public string Socks5Proxy { get; set; }

        /// <summary>
        /// SOCKS5 netWork
        /// </summary>
        [NameInMap("socks5NetWork")]
        [Validation(Required=false)]
        public string Socks5NetWork { get; set; }

    }

}
