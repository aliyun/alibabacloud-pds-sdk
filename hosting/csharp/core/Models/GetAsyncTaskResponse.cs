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

    }

}
