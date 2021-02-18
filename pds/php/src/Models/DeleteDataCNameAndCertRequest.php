<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class DeleteDataCNameAndCertRequest extends Model
{
    /**
     * @description cn-shanghai data cname
     *
     * @example cn-beijing-data.yoursite.com
     *
     * @var string
     */
    public $dataCname;

    /**
     * @description domain ID
     *
     * @example sz100
     *
     * @var string
     */
    public $domainId;

    /**
     * @description location
     *
     * @example cn-beijing
     *
     * @var string
     */
    public $location;
    protected $_name = [
        'dataCname' => 'data_cname',
        'domainId'  => 'domain_id',
        'location'  => 'location',
    ];

    public function validate()
    {
        Model::validateRequired('dataCname', $this->dataCname, true);
        Model::validateRequired('domainId', $this->domainId, true);
        Model::validateRequired('location', $this->location, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->dataCname) {
            $res['data_cname'] = $this->dataCname;
        }
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }
        if (null !== $this->location) {
            $res['location'] = $this->location;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return DeleteDataCNameAndCertRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['data_cname'])) {
            $model->dataCname = $map['data_cname'];
        }
        if (isset($map['domain_id'])) {
            $model->domainId = $map['domain_id'];
        }
        if (isset($map['location'])) {
            $model->location = $map['location'];
        }

        return $model;
    }
}
