// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * Get AsyncTask Response
     */
    public class GetAsyncTaskResponse : TeaModel {
        /// <summary>
        /// async_task_id
        /// type:string
        /// </summary>
        [NameInMap("async_task_id")]
        [Validation(Required=false)]
        public string AsyncTaskId { get; set; }

        /// <summary>
        /// consumed_process
        /// </summary>
        [NameInMap("consumed_process")]
        [Validation(Required=false)]
        public long? ConsumedProcess { get; set; }

        /// <summary>
        /// err_code
        /// </summary>
        [NameInMap("err_code")]
        [Validation(Required=false)]
        public long? ErrCode { get; set; }

        /// <summary>
        /// message
        /// </summary>
        [NameInMap("message")]
        [Validation(Required=false)]
        public string Message { get; set; }

        /// <summary>
        /// state
        /// </summary>
        [NameInMap("state")]
        [Validation(Required=false)]
        public string State { get; set; }

        /// <summary>
        /// total_process
        /// </summary>
        [NameInMap("total_process")]
        [Validation(Required=false)]
        public long? TotalProcess { get; set; }

        /// <summary>
        /// download_url
        /// example
        /// </summary>
        [NameInMap("url")]
        [Validation(Required=false)]
        public string Url { get; set; }

    }

}
