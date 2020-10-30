<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\Hosting\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * DRM License response.
 */
class HostingVideoDRMLicenseResponse extends Model
{
    /**
     * @description drm_data
     *
     * @example xxx
     *
     * @var string
     */
    public $data;

    /**
     * @description states
     *
     * @example 0
     *
     * @var int
     */
    public $states;
    protected $_name = [
        'data'   => 'data',
        'states' => 'states',
    ];

    public function validate()
    {
        Model::validateRequired('data', $this->data, true);
        Model::validateRequired('states', $this->states, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->data) {
            $res['data'] = $this->data;
        }
        if (null !== $this->states) {
            $res['states'] = $this->states;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return HostingVideoDRMLicenseResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['data'])) {
            $model->data = $map['data'];
        }
        if (isset($map['states'])) {
            $model->states = $map['states'];
        }

        return $model;
    }
}
